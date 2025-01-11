import markdown

class FileConverter:
    def __init__(self, argList):
        self.command = argList[1]
        self.inputPath = argList[2]
        self.outputPath = argList[3]

    def validation(self, argList):
        if len(argList) != 4:
            raise ValueError("invalid argument")
        if type(argList[1]) is not str:
            raise TypeError("command must be str")
        if type(argList[2]) is not str:
            raise TypeError("inputPath must be str")
        if type(argList[3]) is not str:
            raise TypeError("outputPath must be str")

    def readContent(self):
        with open(self.inputPath, "r") as f:
            return f.read()

    def convertMarkdownToHtml(self, contents):
        html = markdown.markdown(contents)
        with open(self.outputPath, "w") as f:
            f.write(html)

    def execute(self):
        self.convertMarkdownToHtml(self.readContent())
