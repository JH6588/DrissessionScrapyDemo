from  scrapy import Request

class DrissessionPageRequest(Request):
    """Scrapy ``Request`` subclass providing additional arguments"""

    def __init__(self, is_page=True, screenshot=False, script=None, *args, **kwargs):
        self.is_page = is_page
        self.screenshot = screenshot
        self.script = script

        super().__init__(*args, **kwargs)