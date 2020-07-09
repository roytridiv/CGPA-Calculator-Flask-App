from flask import Flask, render_template , request



def is_number(n):
    try:
        float(n)   
    except ValueError:
        return False
    return True

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/result',methods = ['POST'])
def result():
   if request.method == 'POST':
      credit =request.form['cur_credit']
      cgpa = request.form['cur_cgpa']

      credit_1 = "0"+request.form['credit_1']
      credit_2 = "0"+request.form['credit_2']
      credit_3 = "0"+request.form['credit_3']
      credit_4 = "0"+request.form['credit_4']

      gpa_1 = "0"+request.form['gpa_1']
      gpa_2 = "0"+request.form['gpa_2']
      gpa_3 = "0"+request.form['gpa_3']
      gpa_4 = "0"+request.form['gpa_4']

      if is_number(credit) and is_number(cgpa):
          if is_number(credit_1 +credit_2+credit_3+credit_4+gpa_1+gpa_2+gpa_3+gpa_4):

              if float(credit_1 +credit_2+credit_3+credit_4+gpa_1+gpa_2+gpa_3+gpa_4) == 0:
                  return render_template('result.html', total_cgpa= cgpa , total_gpa = 0)
              else:
                  credit = float(credit)
                  cgpa = float(cgpa)

                  credit_1 = float(credit_1)
                  credit_2 = float(credit_2)
                  credit_3 = float(credit_3)
                  credit_4 = float(credit_4)

                  gpa_1 = float(gpa_1)
                  gpa_2 = float(gpa_2)
                  gpa_3 = float(gpa_3)
                  gpa_4 = float(gpa_4)

                  cur_sum = (credit_1*gpa_1)+(credit_2*gpa_2)+(credit_3*gpa_3)+(credit_4*gpa_4)

                  cur_credit = credit_1+credit_2+credit_3+credit_4


                  total_sum = cur_sum+(cgpa*credit)

                  total_credit = credit + credit_1+ credit_2+ credit_3+ credit_4

                  result_gpa = cur_sum/cur_credit
                  final_result = total_sum/total_credit
                  print("HOLA INPUT FOUND -> ",result_gpa, final_result)
                  return render_template('result.html', total_cgpa= round(final_result,2) , total_gpa = round(result_gpa,4))
              
            
          else:

              return render_template('result.html', total_cgpa= "NaN" , total_gpa = "NaN")
      else:
          return render_template('result.html', total_cgpa= "NaN" , total_gpa = "NaN")
      


      

      






if __name__ == '__main__':
    app.run(debug=True)
