| No.   | Aktif | Nilai Memenuhi | Prasyarat | Pengalaman | Sertifikat | Hasil `lulus` | Hasil `prioritas` | Output                                    |
|---|---|---|---|---|---|---|---|---|
| **1** | True  | False          | True      | False      | True       | False         | True              | **TIDAK LULUS**, mendapat PRIORITAS       |
| **2** | True  | True           | True      | False      | True       | True          | True              | **LULUS**, mendapat PRIORITAS             |
| **3** | False | False          | False     | False      | False      | False         | False             | **TIDAK LULUS**, tidak mendapat prioritas |
| **4** | True  | True           | True      | True       | True       | True          | True              | **LULUS**, mendapat PRIORITAS             |
| **5** | True  | True           | True      | True       | False      | True          | True              | **LULUS**, mendapat PRIORITAS             |
| **6** | True  | True           | True      | False      | True       | True          | True              | **LULUS**, mendapat PRIORITAS             |
| **7** | True  | True           | True      | False      | True       | True          | True              | **LULUS**, mendapat PRIORITAS             |
| **8** | True  | True           | True      | False      | True       | True          | True              | **LULUS**, mendapat PRIORITAS             |

| No. | Nilai | Kehadiran | Output | Logika |
|---|---|---|---|---|
| 1 | T | T | T | AND |
| 2 | T | F | F | AND |
| 3 | F | T | F | AND |

| No. | Akademik | Nonakademik | Output | Logika |
|---|---|---|---|---|
| 1 | F | T | T | OR |
| 2 | T | F | T | OR |
| 3 | F | F | F | OR |
