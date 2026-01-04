from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        results = []

        #Injeção de código para mudar o funcionamento do objeto com a propriedade solution.
        #Set captura no console, o qual é interceptado pelo listener configurado com playwright,
        #e o valor é salvo em outra variável no objeto, para evitar loop. Essa é fornecida no get.
        codigo_js = """
        window._palavras_capturadas = new Set(); 
        Object.defineProperty(Object.prototype, 'solution', {
            set: function(val) {
                if (typeof val === 'string' && val.length === 5) {
                    if (!window._palavras_capturadas.has(val)) {
                        console.log("CAPTURA:" + val);
                        window._palavras_capturadas.add(val);
                    }
                }
                this._val = val;
            },
            get: function() { return this._val; },
            configurable: true
        });
        """

        page.add_init_script(codigo_js)

        page.on("console", lambda msg: results.append(msg.text.split(':')[1]) if "CAPTURA:" in msg.text else None)

        modes = [
            ("Termo", "https://term.ooo/"),
            ("Dueto", "https://term.ooo/2"),
            ("Quarteto", "https://term.ooo/4"),
        ]
        
        for mode, url in modes:
            results.clear()
            page.goto(url)
            page.wait_for_load_state("networkidle")
            print(f"{mode}: {", ".join(results)}")

if __name__ == "__main__":
    run()