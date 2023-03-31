from flask import Flask, request, render_template
from apyori import apriori
import pandas as pd
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/upload')
def uplaod():
    return render_template('upload.html')

@app.route('/apriori', methods=['POST'])
def apriori_results():
    # Parse the CSV data from the user's upload
    data = request.files['file'].read().decode('utf-8')
    data = [line.split(',') for line in data.split('\n')]
    
    # Run the Apriori algorithm
    results = apriori(transactions=data, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2, max_length = 2)
    
    # Return the frequent itemsets to the user
    return render_template('apriori.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)










# @app.route('/apriori', methods=['POST'])
# def apriori_results():
#     # Parse the CSV data from the user's upload
#     data = request.files['file'].read().decode('utf-8')
#     sup = request.form.get('support')
#     conf = request.form.get('confidence')
#     # data = [line.split(',') for line in data.split('\n')]
#     records = []
#     for i in range(data.shape[0]):
#         records.append([str(data.values[i, j]).split(',') for j in range(data.shape[1])])

#     dataKerja = []
#     for record in records:
#         dataKerja.append(record[1:])
    
#     min_sup = float('0.00' + str(sup))
#     min_conf = float('0.00' + str(conf))
#     # Run the Apriori algorithm
#     results = apriori(dataKerja, min_support = min_sup, min_confidence = min_conf, min_lift = 3, min_length = 2, max_length = 2)
#     association_results = list(results)
#     # Return the frequent itemsets to the user
#     pd.set_option('max_colwidth', 200)
#     result = pd.DataFrame(columns=['Rule', 'Support', 'Confidence'])

#     for item in association_results:
#         pair = item[2]
#     for i in pair:
#         antecedent = ", ".join([str(x) for x in i[0]])
#         consequent = ", ".join([str(x) for x in i[1]])
#         result = result.append({
#             'Rule': antecedent + " -> " + consequent,
#             'Support': str(round(item[1] * 100, 2)) + '%',
#             'Confidence': str(round(i[2] * 100, 2)) + '%'
#         }, ignore_index=True)
#     return render_template('apriori.html', name='made', sup = sup, conf = conf, len= len(result)-1,  query = result)

# @app.route('/apriori', methods=['POST'])
# def apriori_results():
#     # Parse the CSV data from the user's upload
#     data = request.files['file'].read().decode('utf-8')
#     sup = request.form.get('support')
#     conf = request.form.get('confidence')
    
#     # Split the data into lines and then split each line into items
#     data = [line.split(',') for line in data.split('\n') if line.strip()]
    
#     # Convert the data into a list of transactions
#     transactions = [[item.strip() for item in line] for line in data]
    
#     min_sup = float('' + str(sup))
#     min_conf = float('' + str(conf))
    
#     # Run the Apriori algorithm
#     results = apriori(transactions=transactions, min_support=min_sup, min_confidence=min_conf, min_lift=3, min_length=2, max_length=2)
#     association_results = list(results)
#     # Convert the results into a DataFrame for display
#     pd.set_option('max_colwidth', 200)
#     result = pd.DataFrame(columns=['Rule', 'Support', 'Confidence'])
    
#     for item in association_results:
#         pair = item[2][0]
#         antecedent = ", ".join([str(x) for x in pair[0]])
#         consequent = ", ".join([str(x) for x in pair[1]])
#         result = result.append({
#             'Rule': antecedent + " -> " + consequent,
#             'Support': str(round(item[1] * 100, 2)) + '%',
#             'Confidence': str(round(item[2][0][2] * 100, 2)) + '%'
#         }, ignore_index=True)
    
#     return render_template('result.html', name='made', sup=sup, conf=conf, num_results=len(result)-1, query=result)











