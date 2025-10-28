from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_add_to_cart_button(browser, request):
    browser.get(link)
    button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary"))
    )
    user_language = request.config.getoption("language")
    expected_texts = {
        "ru": "Добавить в корзину",
        "fr": "Ajouter au panier",
        "es": "Añadir al carrito",
        "en-gb": "Add to basket"
    }
    assert button.text == expected_texts.get(user_language)

