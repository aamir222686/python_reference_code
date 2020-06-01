import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
df = pd.read_csv('iris.csv')
app = dash.Dash()
app.layout =html.Div(children=[
	html.H1(children = 'My Dash Application'),
	html.H2(children= 'First Line'),
	dcc.Graph(
			id='example', figure={'data' : [{'x': df['species'], 'type': 'bar', 'name': 'some name'}]}
		)
	])
if __name__ == '__main__':
	app.run_server(debug=True)
