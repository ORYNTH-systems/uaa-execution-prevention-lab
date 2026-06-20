\# UAA Execution Prevention Lab — Demo Instructions



\## Requirements



\* Python 3.11+

\* Git



\---



\## Clone Repository



```powershell

git clone https://github.com/ORYNTH-systems/uaa-execution-prevention-lab.git

cd uaa-execution-prevention-lab

```



\---



\## Run Full Evidence Corpus



```powershell

python src\\main.py --all

```



Expected Result:



```text

Total Demonstrations: 10

Total Prevented Failures: 10

Prevention Rate: 100%

```



\---



\## Run Individual Demonstration



Example:



```powershell

python src\\main.py --case EP-004

```



This executes only the selected demonstration.



\---



\## JSON Evidence Output



Evidence files are generated under:



```text

reports/json/

```



Example:



```text

reports/json/EP-004.json

```



Each record contains:



\* Case identifier

\* Admissibility result

\* Execution result

\* Failure-prevention status

\* Triggered violations



\---



\## Assertions



Each demonstration executes deterministic validation checks.



Example:



```python

assert result.execution\_result == "DECLINED"

assert result.failure\_prevented is True

```



\---



\## Repository Verification



```powershell

git status

```



Expected:



```text

nothing to commit, working tree clean

```



