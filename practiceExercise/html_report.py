import os
import datetime
import js2py


def createReportFile():
    global reportFile

    # folderName = str(datetime.datetime.date(datetime.datetime.now()))
    # if not os.path.exists(r'..\\Reports\\' + folderName):
    #     os.mkdir(r'..\\Reports\\' + folderName)
    # filename = filename + '_' + str(datetime.datetime.now()).replace(" ", "_").replace(":", "").replace(".", "") \
    #     .replace("-", "")
    # path = folderName + '\\' + filename
    reportFile = open(r'C:\\pyCharmProjects\\learningPython\\report.html', 'a')
    message = """<html>
                    <head>
                        <style>
                            table, td {
                                border: 1px solid black;
                                        }
                        </style>
                    </head>
                    <body>
                        <p>Click the button to add a new row at the first position of the table and then add cells and content.</p>
                        
                        <table id="TAReportTable"></table>
                    </body>
                </html>"""
    reportFile.write(message)


jsCode = '''function addReportRow() 
            {
              var table = document.getElementById("TAReportTable");
              var row = table.insertRow(0);
              var cell1 = row.insertCell(0);
              var cell2 = row.insertCell(1);
              cell1.innerHTML = "NEW CELL1";
              cell2.innerHTML = "NEW CELL2";
            }'''


def reportText(text, state, additionalInfo=""):
    if state == 'pass':
        write_green(text + " " + additionalInfo)
    elif state == 'info':
        write_blue(text + " " + additionalInfo)
    else:
        write_red(text + " " + additionalInfo)


def write_red(str_):
    js2py.eval_js(jsCode)
    # reportFile.write('<div style="background-color:#F95369; color:#000000">%s</div>' % str_)


def write_blue(str_):
    js2py.eval_js(jsCode)
    # reportFile.write('<div style="background-color:#43EDFF; color:#000000">%s</div>' % str_)


def write_green(str_):
    js2py.eval_js(jsCode)
    # reportFile.write('<div style="background-color:#34C939; color:#000000">%s</div>' % str_)


# def write_orange(str_):
#     reportFile.write('<div style="background-color:#ffa500; color:#000000">%s</div>' % str_)


createReportFile()
reportText('sohsn', 'pass')
