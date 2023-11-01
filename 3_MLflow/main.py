import pandas as pd
import mlflow
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import mlflow.sklearn
from mlflow.models import infer_signature

archivo = "automobileEDA.csv"
df = pd.read_csv(archivo)
#print(df.head(5))

mlflow.set_experiment("Experimento_regresión_lineal")
mlflow.set_tracking_uri("http://127.0.0.1:5000/")

X = df[['curb-weight','engine-size']]
y = df[['price']].values.reshape(-1,1)
#print(X)
#print(Y)


with mlflow.start_run() as run:
    params = {"test_size":0.3,"random_state":3}
    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=params["test_size"],
                                                        random_state=params["random_state"])
    LinearM = LinearRegression()
    LinearM.fit(X_train,y_train)
    weights=LinearM.coef_
    intercept = LinearM.intercept_
    y_pred = LinearM.predict(X_test)
    R2 = LinearM.score(X_test,y_test)
    signature = infer_signature(X_test,y_pred)
    mlflow.log_param("R2",R2)
    mlflow.log_params(params)
    mlflow.log_metrics({
     "mse": mean_squared_error(y_test,y_pred),
     "mae": mean_absolute_error(y_test,y_pred),
     "r2": r2_score(y_test,y_pred)
    })
    mlflow.sklearn.log_model(
        sk_model=LinearM,
        artifact_path="sklear-model",
        signature=signature,
        registered_model_name = "mlflow_clase_lregression_model"
        
        )
    pass

 