import os
from jinja2 import Environment, FileSystemLoader


class PerformanceReport:
    """ Report with performance stats for given strategy returns.
    """

    def __init__(self):
        pass
 
    def generate_html(self):
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template("templates/template.html")
        placeholder = 'Hello World'
        html_out = template.render(test_variable=placeholder)
        return html_out
           
    def generate_html_report(self):
        """ Returns HTML report with analysis
        """
        html = self.generate_html()
        outputdir="output"
        outfile = os.path.join(outputdir, 'report.html')        
        file = open(outfile,"w")  
        file.write(html)
        file.close()         

if __name__ == "__main__":
    report = PerformanceReport()
    report.generate_html_report()