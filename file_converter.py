import markdown

class FileConverter:
    def __init__(self, argList):
        self.command = argList[1]
        self.inputPath = argList[2]
        self.outputPath = argList[3]

    def readContent(self):
        with open(self.inputPath, "r") as f:
            return f.read()

    def convertMarkdownToHtml(self, contents):
        html = markdown.markdown(contents)
        with open(self.outputPath, "w") as f:
            f.write(html)

    def execute(self):
      self.convertMarkdownToHtml(self.readContent())