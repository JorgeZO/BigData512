"""Ejemplo reproducible de KNN: seleccionar k con CV y reservar prueba."""
from pathlib import Path
import json
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix


def main():
    iris = load_iris(as_frame=True)
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=.30, random_state=82005, stratify=iris.target)
    pipeline = make_pipeline(StandardScaler(), KNeighborsClassifier())
    validacion = StratifiedKFold(n_splits=5, shuffle=True, random_state=82005)
    busqueda = GridSearchCV(pipeline, {"kneighborsclassifier__n_neighbors": [1, 3, 5, 7, 9, 11]},
                           scoring="f1_macro", cv=validacion)
    busqueda.fit(X_train, y_train)
    predicciones = busqueda.predict(X_test)
    resultados = {"dataset": "Iris incluido en scikit-learn", "semilla": 82005,
                  "filas_entrenamiento": len(X_train), "filas_prueba": len(X_test),
                  "k": busqueda.best_params_["kneighborsclassifier__n_neighbors"],
                  "f1_cv": float(busqueda.best_score_),
                  "accuracy_prueba": float(accuracy_score(y_test, predicciones)),
                  "f1_macro_prueba": float(f1_score(y_test, predicciones, average="macro")),
                  "clases": iris.target_names.tolist(),
                  "matriz_confusion": confusion_matrix(y_test, predicciones).tolist()}
    raiz = Path(__file__).resolve().parents[1]
    destino = raiz / "reportes/knn_resultados.json"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps(resultados, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(resultados, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
