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
    contact_header = By.ID, 'contact-link'
    contact_form_email = By.ID, 'email'
    contact_form_id_order = By.ID, 'id_order'
    contact_form_message = By.ID, 'message'
    contact_form_fileUpload = By.ID, 'fileUpload'
    contact_form_id_contact = By.ID, 'id_contact'
    contact_form_id_contact_value_webmaster = '1'
    contact_form_id_contact_value_customer_service = '2'
    contact_form_send_button = By.ID, 'submitMessage'
    alert_error = By.CLASS_NAME, 'alert-danger'
    alert_success = By.CLASS_NAME, 'alert-success'