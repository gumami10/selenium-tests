from selenium.webdriver.common.by import By


class MyStoreLocators:
    search_bar = By.ID, 'search_query_top'
    submit_search = By.NAME, 'submit_search'
    products_result_search_title = By.CSS_SELECTOR, 'ul.product_list .product-name'
    add_to_cart = By.CSS_SELECTOR, '.ajax_add_to_cart_button'
    cart_header_quantity = By.CSS_SELECTOR, '.ajax_cart_quantity'
    continue_to_shopping = By.CSS_SELECTOR, '.continue'
    checkout_header_cart = By.ID, 'button_order_cart'
    cart_summary = By.ID, 'cart_summary'
    header_cart_remove_item = By.CSS_SELECTOR, '.ajax_cart_block_remove_link'
    header_cart_no_item = By.CSS_SELECTOR, '.ajax_cart_no_product'