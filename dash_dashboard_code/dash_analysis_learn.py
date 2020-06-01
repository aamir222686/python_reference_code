import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html 
app =dash.Dash()

app.layout = html.Div([
			dcc.Input(id = 'input', placeholder='Enter Something Here', type='text'),
			html.Div(id='output')


	])

if __name__ == '__main__':
	app.run_server(debug=True)