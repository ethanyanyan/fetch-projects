import pandas as pd
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

def load_and_process_data(filename):
    data = pd.read_csv(filename)
    data['Day_of_year'] = data['# Date'].apply(lambda x: pd.to_datetime(x).dayofyear)
    return data

def split_data(data, start_date):
    start_day = pd.to_datetime(start_date).dayofyear
    train_data = data[data['Day_of_year'] < start_day]
    val_data = data[data['Day_of_year'] >= start_day]
    return train_data, val_data

def train_model(model, X_train, y_train, X_val, y_val, num_epochs=200000, fine_tune_epochs=50000):
    criterion = nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.00002)
    optimizer_ft = torch.optim.SGD(model.parameters(), lr=0.0000001)

    for epoch in range(num_epochs):
        optimizer.zero_grad()
        outputs = model(X_train)
        loss = criterion(outputs, y_train)
        loss.backward()
        optimizer.step()

        if (epoch+1) % 20000 == 0:
            with torch.no_grad():
                val_outputs = model(X_val)
                val_loss = criterion(val_outputs, y_val)
            print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}, Val Loss: {val_loss.item():.4f}')

    for epoch in range(fine_tune_epochs):
        optimizer_ft.zero_grad()
        outputs = model(X_val)
        loss = criterion(outputs, y_val)
        loss.backward()
        optimizer_ft.step()
        if (epoch+1) % 10000 == 0:
            print(f'Fine-tune Epoch [{epoch+1}/{fine_tune_epochs}], Loss: {loss.item():.4f}')

    return model

def plot_results(X_train, y_train, X_val, y_val, days_2022, predictions_2022):
    plt.scatter(X_train, y_train, label='Training data', color='blue', s=8)
    plt.scatter(X_val, y_val, label='December data', color='green', s=8)
    plt.scatter(days_2022, predictions_2022, label='Predictions for 2022', color='red', s=8)
    plt.xlabel('Day of Year')
    plt.ylabel('Receipt Count')
    plt.title('Receipt Analysis')
    plt.legend()
    plt.grid(True)
    plt.show()

data = load_and_process_data("fetch_data_daily.csv")
train_data, val_data = split_data(data, "2021-12-01")

X_train = torch.FloatTensor(train_data[['Day_of_year']].values)
y_train = torch.FloatTensor(train_data['Receipt_Count'].values / 1e6).view(-1, 1)
X_val = torch.FloatTensor(val_data[['Day_of_year']].values)
y_val = torch.FloatTensor(val_data['Receipt_Count'].values / 1e6).view(-1, 1)

class LinearRegression(nn.Module):
    def __init__(self, input_dim):
        super(LinearRegression, self).__init__()
        self.linear = nn.Linear(input_dim, 1)

    def forward(self, x):
        return self.linear(x)

model = LinearRegression(1)
model = train_model(model, X_train, y_train, X_val, y_val)

with torch.no_grad():
    days_2022 = torch.FloatTensor([[i] for i in range(366, 731)]).view(-1, 1)
    predictions_2022 = model(days_2022).numpy() * 1e6

# plot_results(X_train.numpy(), (y_train * 1e6).numpy(), X_val.numpy(), (y_val * 1e6).numpy(), days_2022.numpy(), predictions_2022)

torch.save(model.state_dict(), 'linear_regression_model.pth')


def get_monthly_predictions():
    # Days in each month of 2022
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    monthly_sums = []
    start_index = 0

    # Sum up the predictions for each month
    for days in month_days:
        monthly_sums.append(int(sum(predictions_2022[start_index:start_index + days])))
        start_index += days

    return monthly_sums
