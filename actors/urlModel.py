from Jumpscale import j


JSBASE = j.application.JSBaseClass



class url(JSBASE):
    def __init__(self, *args, **kwarsg):
        self.bcdb = j.data.bcdb.get("url_test")
        self.model = self.bcdb.model_get(url="threefold.grid.url")

    def ping(self):
        True

    def addUrl(self, tinyUrl, originalUrl, schema_out):
        """
        ```in
        tinyUrl = (S)
        originalUrl = (I)
        ```
        ```out
        success = "" (B)
        ```
        """
        model_obj = self.model.new()
        model_obj.tinyUrl = tinyUrl
        model_obj.originalUrl = originalUrl
        model_obj.save()

        out = schema_out.new()
        out.success = True
        return out

    # def get_url(self, name, schema_out):
    #     """
    #     ```in
    #     name = (S)
    #     ```
    #     ```out
    #     !threefold.grid.sarah.person
    #     ```
    #     """

    #     return self.model.find(name=name)[0]

    def send(self, message):
        return message