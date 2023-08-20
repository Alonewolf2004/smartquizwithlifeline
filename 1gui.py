import PySimpleGUI as tr

conversion_rates = {
    'EUROS': {
        'POUNDS': 0.85,
        'YENS': 130.2,
        'USD': 1.18,
        'RS': 88.25
    },
    'POUNDS': {
        'EUROS': 1.18,
        'YENS': 153.4,
        'USD': 1.37,
        'RS': 102.74
    },
    'YENS': {
        'EUROS': 0.0063,
        'POUNDS': 0.0054,
        'USD': 0.0069,
        'RS': 0.5723
    },
    'USD': {
        'EUROS': 0.85,
        'POUNDS': 0.73,
        'YENS': 145.3346,
        'RS': 74.45
    },
    'RS': {
        'EUROS': 0.0113,
        'POUNDS': 0.0097,
        'YENS': 1.7475,
        'USD': 0.0134
    }
}

layout = [
    [tr.Text("SELECT FROM"), tr.Spin(['EUROS', 'POUNDS', 'YENS', 'USD', 'RS'], key='from_country')],
    [tr.Text("SELECT TO"), tr.Spin(['EUROS', 'POUNDS', 'YENS', 'USD', 'RS'], key='to_country')],
    [tr.Button("ENTER The Amount"), tr.Input(key='amount')],
    [tr.Text('Converted Amount:',key='convert')]
]

window = tr.Window("converter", layout)

while True:
    event, values = window.read()

    if event == tr.WIN_CLOSED:
        break
    if event == 'ENTER The Amount':
        from_country = values["from_country"]
        to_country = values['to_country']
        amount = float(values['amount'])  # Convert amount to a float

        if from_country == to_country:
            converted_amount = amount
        else:
            conversion_rate = conversion_rates[from_country][to_country]
            converted_amount = amount * conversion_rate
        window['convert'].update(f'Converted Amount: {converted_amount:.2f}')

window.close()
