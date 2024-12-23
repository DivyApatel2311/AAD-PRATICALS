from flask import Flask, render_template
import plotly.graph_objs as go
import plotly.offline as pyo

app = Flask(__name__)

def min_coins(coins, value):
    # Initialize the dp array where dp[i] is the minimum number of coins for value i
    dp = [float('inf')] * (value + 1)
    dp[0] = 0  # Base case: no coins are needed for value 0
    
    for i in range(1, value + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)  # Take the minimum coin count
    
    return dp[value] if dp[value] != float('inf') else -1  # Return -1 if no solution

@app.route('/')
def index():
    coins = [10, 20, 50]
    values = list(range(1, 71))  # For demonstration, calculate from Rs. 1 to Rs. 20
    results = [min_coins(coins, value) for value in values]  # Get min coins for each value
    
    # Create a Plotly graph
    trace = go.Scatter(x=values, y=results, mode='lines+markers', name='Min Coins')
    layout = go.Layout(
        title='Minimum Coins Required for Different Values',
        xaxis=dict(title='Value (Rs.)'),
        yaxis=dict(title='Number of Coins')
    )
    fig = go.Figure(data=[trace], layout=layout)
    
    # Render the plot as HTML
    plot_html = pyo.plot(fig, output_type='div', include_plotlyjs=True)
    
    # Render the HTML page
    return render_template('index.html', plot=plot_html, coins=coins, target_value=9, result=results[8])

if __name__ == '__main__':
    app.run(debug=True)
