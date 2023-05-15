from flask import Flask, render_template, request

app = Flask(__name__)#Экземпляр приложения flask


@app.route('/')#Обозначение, что функция будет отвечать на веб запросы
@app.route('/index')
def index():
    return render_template("index.html")#Импорт html файла


@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        sum = int(request.form.get('num_1'))
        months = int(request.form.get('num_2'))
        procent = int(request.form.get('num_3')) * 0.01
        type = request.form['options']
    if type == '1':#Аннуитентный
        month_pay = round((sum * procent / 12 * pow((1 + procent / 12), months) / (pow((1 + procent / 12), months) - 1)), 2)
        all_pay = month_pay * 12
        all_procent = round((all_pay - sum), 2)
        return render_template('index.html', ans= str("Ежемесячная выплата ≈ " + str(month_pay)), ans1= str("Общая сумма выплат ≈ " + str(all_pay)), ans2= str("Начисленные проценты ≈ " + str(all_procent) ) )

    if type == '2':#Дифференцированный
        i = 0
        ans_template = str('')
        all_pay = 0
        while i < months:
            ostatok = sum - sum / months * (i)
            procent_platezh = round(((ostatok * procent * 31)/ 365), 2)
            month_pay = round((sum / months + procent_platezh), 2)
            ans_template += str("выплата в " + str(i + 1) + "-м месяце ≈ " + str(month_pay) + ", ")
            all_pay += month_pay
            i += 1
        all_procent = round(all_pay - sum, 2)
        return render_template('index.html', ans= ans_template, ans1= str('Общая сумма выплат ≈ ' + str(all_pay)), ans2= str('Начисленные проценты ≈ ' + str(all_pay - sum)))
    else:
        return render_template('index.html', ans='Укажите тип платежа!')

if __name__ == '__main__':
    app.run()
