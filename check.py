from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

y_true = [...]  # ground truth labels
y_pred = [...]  # model predictions

cm = confusion_matrix(y_true, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=list(idx_to_class.values()))
disp.plot()
