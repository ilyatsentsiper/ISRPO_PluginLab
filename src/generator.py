from java.lang import Runnable

from com.intellij.openapi.actionSystem import AnAction
from com.intellij.openapi.command import WriteCommandAction
from com.intellij.openapi.fileEditor import FileEditorManager


class GeneratePipelineAction(AnAction):
    def actionPerformed(self, event):
        project = event.getProject()
        if not project:
            return

        editor = FileEditorManager.getInstance(project).getSelectedTextEditor()
        if not editor:
            return

        document = editor.getDocument()
        offset = editor.getCaretModel().getOffset()

        # Шаблон готового ML-кода
        ml_code = (
            "import pandas as pd\n"
            "from sklearn.model_selection import train_test_split\n"
            "from sklearn.ensemble import RandomForestClassifier\n"
            "from sklearn.metrics import classification_report\n\n"
            "# 1. Dataset loading\n"
            "df = pd.read_csv('dataset.csv')\n"
            "X = df.iloc[:, :-1]\n"
            "y = df.iloc[:, -1]\n\n"
            "# 2. Split data\n"
            "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n\n"
            "# 3. Fit model\n"
            "model = RandomForestClassifier()\n"
            "model.fit(X_train, y_train)\n\n"
            "# 4. Report\n"
            "preds = model.predict(X_test)\n"
            "print(classification_report(y_test, preds))\n"
        )

        class InsertRunnable(Runnable):
            def run(self):
                document.insertString(offset, ml_code)

        WriteCommandAction.runWriteCommandAction(project, InsertRunnable())
