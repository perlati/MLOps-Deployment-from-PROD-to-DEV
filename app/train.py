import mlflow, random
if __name__ == "__main__":
    mlflow.set_experiment("lab-exp")
    with mlflow.start_run(run_name="trial"):
        acc = 0.8 + random.random()*0.1
        mlflow.log_metric("accuracy", acc)
        mlflow.log_param("model_type", "toy")
        # save a pseudo "model"
        with open("model.txt","w") as f: f.write(f"acc={acc:.4f}\n")
        mlflow.log_artifact("model.txt")
