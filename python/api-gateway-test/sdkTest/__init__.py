from config import TEST_RESULTS_TABLE_NAME

Hash = {}

def engageTest(*hashKeys):
    def dec(func):
        def wrapper(self, *args, **kwargs):
            for key in hashKeys:
                if key not in Hash:
                    print(f"Function {func.__name__} has ignored, due to {key} not found in hash map!")
                    return
            if not self.base.is_authed:
                self.base.auth()
            test_name, success, detail = func.__name__, True, None
            try:
                func(self, *args, **kwargs)
            except Exception as e:
                success = False
                detail = repr(e)
            self.base.append_row(TEST_RESULTS_TABLE_NAME, self.format_infos(test_name, success, detail))
        return wrapper
    return dec