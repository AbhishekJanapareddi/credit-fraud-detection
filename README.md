# Credit Transactions fraud detection (Anomaly detection)

<h2>Primary focus:</h2>
<ul>
  <li>Model selection</li>
  <li>Deployment</li>
  <li>Anomaly detection</li>
</ul>

<h2>Steps followed:</h2>
<ul>
  <li>Data Preprocessing</li>
  <li>Model Selection</li>
  <li>Model training</li>
  <li>Model deployment</li>
</ul>

<h2>Steps skipped:</h2>
<ul>
  <li>Cross validation</li>
  <li>Hyperparameter tuning</li>
  <li>Feature Engineering</li>
  <li>Visualizations</li>
</ul>

<h2>Observations:</h2>
<ul>
  <li>Obs 1: Logistic Regression has a huge number of false positives (Lesser precision and Accuracy) </li>
  <li>Obs 2: Local Outlier Factor has higher percentage of false negatives</li>
  <li>Obs 3: Undersampling and Oversampling do not help</li>
  <li>Obs 4: Focused on reducing False Negative (Increasing recall) than False positive (Precision) as it is important to find as many fraud txs as possible while predicting some real txs as fraud might not hurt.</li>
</ul>
