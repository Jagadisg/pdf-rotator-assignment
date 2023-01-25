from flask import Flask, request, jsonify,render_template
import pikepdf
app = Flask(__name__,template_folder='template')
@app.route('/')
def page():
    return render_template("index.html")

@app.route('/rotate_pdf', methods=['POST'])
def rotate_pdf():
    # get inputs from user
    file_path = request.form.get('file_path')
    angle_of_rotation = int(request.form.get('angle_of_rotation'))
    page_number = int(request.form.get('page_number'))
    sample_pdf = pikepdf.Pdf.open(file_path)
    for i in range(1,(len(sample_pdf.pages)+1)):
        if i == page_number:
            res = sample_pdf.pages[i-1]
            res.rotate(angle_of_rotation, True)
    sample_pdf.save("newsample.pdf")


    return jsonify(file_path='newsample.pdf')

if __name__ == '__main__':
    app.run(debug=True)
