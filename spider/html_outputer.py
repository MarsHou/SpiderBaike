# -*- coding: utf-8 -*-
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_date(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w', encoding='utf-8')
        fout.write(r'<meta http-equiv=Content-Type content="text/html;charset=utf-8">')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table border='1'>")
        for data in self.datas:
            fout.write("<tr>")
            # fout.write("<td>%s</td>" % data["url"])
            fout.write("<td><a href='%s'>%s</a></td>" % (data["url"],data["title"]))
            fout.write("<td>%s</td>" % data["summary"])
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
