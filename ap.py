import pdfkit


path_to_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"

url= "https://www.google.com/"

config = pdfkit.configuration(wkhtmltopdf = path_to_wkhtmltopdf )

pdfkit.from_url(url ,output_path = 'webpage.pdf' , configuration = config)

# def conver_html_to_pdf(html_page,save_name):
#     pdfkit.from_url(html_page , save_name)
#     # pdfkit.from_file()    



# conver_html_to_pdf("https://www.google.com/", "out.pdf")
























# from flask import  Flask, make_response , render_template
# import pdfkit

# app=Flask(__name__)

# # config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
# config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')

# @app.route("/<name>")
# def home(name):
#     res =render_template('index.html', name = name)
#     responseString = pdfkit.from_string(res, False)


#     response=make_response(responseString)
#     response.headers['Content-Type']= 'application/pdf'
#     response.headers['Content-Disposition']= 'inline;filename=output.pdf'
#     response.headers['Content-config']= 'configuration=config'



#     return response






# if __name__ == "__main__":
#     app.run(debug=True)