import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
    let disposable = vscode.commands.registerCommand('ml-generator.generatePipeline', () => {
        const editor = vscode.window.activeTextEditor;
        if (!editor) {
            return;
        }
        const mlCode = `import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# 1. Загрузка данных
df = pd.read_csv('dataset.csv')
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# 2. Разделение выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Обучение ML-модели
model = RandomForestClassifier()
model.fit(X_train, y_train)

# 4. Оценка качества
preds = model.predict(X_test)
print(classification_report(y_test, preds))
`;

        editor.edit((editBuilder: vscode.TextEditorEdit) => {
            editBuilder.insert(editor.selection.active, mlCode);
        });
    });

    context.subscriptions.push(disposable);
}

export function deactivate() {}
