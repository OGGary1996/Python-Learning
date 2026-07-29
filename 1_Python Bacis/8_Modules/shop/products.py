# Python 通常使用单下划线表示内部实现：
def find_products(products_id):
    return _load_products(products_id)

def _load_products(products_id):
    return {"id": products_id}