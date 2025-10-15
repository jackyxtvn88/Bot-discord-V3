# 📊 Hệ Thống Xuất Excel Chi Tiết

## ✨ Tổng Quan

Bot giờ đây có thể **xuất toàn bộ dữ liệu chấm công ra file Excel** với định dạng đẹp mắt, đầy đủ chi tiết và dễ đọc.

## 🎯 Tính Năng

### Xuất Excel Backup

**Command:**
```
/admin export
```

**Quyền:** Administrator

**Kết quả:** File Excel (.xlsx) chứa **6 sheets** chi tiết:

## 📋 Cấu Trúc File Excel

### Sheet 1: 📊 Tóm Tắt
**Nội dung:**
- Thời gian backup
- Thông tin hệ thống
- **Thống kê tổng quan:**
  - Tổng số lần chấm công
  - Tổng số lần nghỉ giải lao
  - Số cấu hình thời gian làm việc
  - Số lần quên chấm công
  - Số ngày nghỉ được đăng ký
- **Top 5 Chấm Công Nhiều Nhất**

**Màu sắc:** Xanh dương chủ đạo

### Sheet 2: ✅ Chấm Công
**Cột:**
- STT
- User ID
- Tên
- Ngày
- Check-in
- Check-out
- Tổng giờ làm
- Thời gian nghỉ
- Ghi chú

**Đặc điểm:**
- ⚠️ Dòng màu vàng: Vi phạm làm thiếu giờ (< 8h)
- Tự động tính tổng giờ làm và giờ nghỉ
- Sắp xếp theo ngày mới nhất

**Màu header:** Xanh dương đậm

### Sheet 3: 🍵 Nghỉ Giải Lao
**Cột:**
- STT
- User ID
- Tên
- Ngày
- Bắt đầu
- Kết thúc
- Thời gian (phút)
- Ghi chú

**Màu header:** Xanh lá

### Sheet 4: ⏰ Thời Gian Làm Việc
**Cột:**
- STT
- User ID
- Tên
- Loại (Mặc định Server / Cá nhân)
- Giờ bắt đầu
- Giờ kết thúc
- Nghỉ tối thiểu
- Nghỉ tối đa

**Màu header:** Cam

### Sheet 5: ❌ Quên Chấm Công
**Cột:**
- STT
- User ID
- Tên
- Ngày
- Loại (Quên Check-in / Quên Check-out / Quên cả 2)
- Lý do
- Trạng thái (Đã xử lý / Chưa xử lý)

**Màu header:** Đỏ

### Sheet 6: 🏖️ Ngày Nghỉ
**Cột:**
- STT
- Ngày
- Loại (Toàn Server / Cá nhân)
- Lý do
- Người tạo

**Màu header:** Tím

## 🚀 Cách Sử Dụng

### 1. Xuất File Excel

```
/admin export
```

**Bot sẽ:**
1. ⏳ Processing... (có thể mất vài giây)
2. ✅ Tạo file Excel
3. 📤 Gửi file trực tiếp cho bạn (DM hoặc ephemeral)
4. 📊 Hiển thị thông tin file:
   - Tên file
   - Kích thước (MB)
   - Danh sách sheets

**Ví dụ response:**
```
✅ Đã xuất dữ liệu thành công!

📁 File: backup_20251009_173000.xlsx
📊 Kích thước: 0.45 MB
📋 Bao gồm:
  • Sheet Chấm Công (Attendance)
  • Sheet Nghỉ Giải Lao (Breaks)
  • Sheet Thời Gian Làm Việc
  • Sheet Quên Chấm Công
  • Sheet Ngày Nghỉ
  • Sheet Tóm Tắt

📥 File đã được lưu tại: backups/backup_20251009_173000.xlsx
```

### 2. Download File

File sẽ được **tự động gửi kèm** trong response Discord. Click để download!

### 3. Mở File

Mở bằng:
- ✅ Microsoft Excel (khuyến nghị)
- ✅ Google Sheets
- ✅ LibreOffice Calc
- ✅ WPS Office

## 📊 Định Dạng Excel

### Font & Style
- **Header:** Font trắng, nền màu, in đậm, size 12
- **Data:** Font đen, size 11
- **Title:** Font trắng, nền xanh đậm, size 16

### Alignment
- **Header:** Canh giữa ngang và dọc
- **Data:** Canh trái (text), canh phải (số)

### Column Width
- Tự động điều chỉnh theo nội dung
- Minimum 15 pixels
- Maximum 35 pixels

### Conditional Formatting
- 🟨 **Màu vàng:** Vi phạm làm thiếu giờ (< 8h)

## 💡 Use Cases

### 1. Báo Cáo Định Kỳ
**Hàng tháng:**
```
/admin export
```
→ Gửi cho HR hoặc quản lý

### 2. Phân Tích Dữ Liệu
- Mở Excel
- Sử dụng PivotTable
- Tạo biểu đồ tùy chỉnh
- Tính toán thống kê

### 3. Kiểm Toán
- So sánh dữ liệu từng tháng
- Phát hiện bất thường
- Xác minh vi phạm

### 4. Backup Định Dạng Đọc Được
- Khác với file .db (binary)
- Excel dễ đọc, dễ chia sẻ
- Không cần công cụ đặc biệt

### 5. Import Vào Hệ Thống Khác
- Export từ Bot
- Import vào phần mềm HR
- Tích hợp với payroll

## 🔧 Chi Tiết Kỹ Thuật

### ExcelExportService

**File:** `services/excel_export_service.py`

**Main Method:**
```python
@staticmethod
def create_backup_excel(filename: str = None) -> str:
    # Tạo workbook
    # Tạo 6 sheets
    # Định dạng cells
    # Lưu file
    return filename
```

**Dependencies:**
```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
```

### Sheet Creation Methods

```python
_create_attendance_sheet()   # Sheet chấm công
_create_breaks_sheet()       # Sheet nghỉ giải lao
_create_worktime_sheet()     # Sheet thời gian làm việc
_create_forgot_sheet()       # Sheet quên chấm công
_create_dayoff_sheet()       # Sheet ngày nghỉ
_create_summary_sheet()      # Sheet tóm tắt
```

### File Naming Convention

```
backup_YYYYMMDD_HHMMSS.xlsx
```

**Ví dụ:**
- `backup_20251009_173000.xlsx`
- `backup_20251010_095500.xlsx`

### Storage Location

```
/backups/
  ├─ backup_20251009_173000.xlsx
  ├─ backup_20251010_095500.xlsx
  └─ ...
```

## 📈 So Sánh: .db vs .xlsx

| Tính năng | .db (SQLite) | .xlsx (Excel) |
|-----------|--------------|---------------|
| **Dễ đọc** | ❌ Cần tools | ✅ Mở trực tiếp |
| **Kích thước** | ✅ Nhỏ | ⚠️ Lớn hơn |
| **Backup chính thức** | ✅ Đầy đủ | ⚠️ Export only |
| **Restore** | ✅ Có thể | ❌ Không thể |
| **Chia sẻ** | ❌ Khó | ✅ Dễ dàng |
| **Phân tích** | ❌ Cần query | ✅ Excel tools |
| **In ấn** | ❌ | ✅ |
| **Tốc độ** | ✅ Nhanh | ⚠️ Chậm hơn |

## 💼 Best Practices

### 1. Backup Định Kỳ

**Khuyến nghị:**
- **Hàng tuần:** `/admin backup` (file .db) - Backup chính thức
- **Hàng tháng:** `/admin export` (file .xlsx) - Báo cáo và lưu trữ

### 2. Đặt Tên File Có Ý Nghĩa

Sau khi download, đổi tên:
```
backup_20251009_173000.xlsx
  ↓
ChamCong_Thang10_2025.xlsx
```

### 3. Lưu Trữ An Toàn

- 💾 Cloud storage (Google Drive, OneDrive)
- 💾 External hard drive
- 💾 NAS server

### 4. Bảo Mật

⚠️ **File Excel chứa thông tin nhạy cảm:**
- User IDs
- Thời gian làm việc
- Vi phạm cá nhân

**Khuyến nghị:**
- Đặt password cho file Excel
- Chỉ chia sẻ với người có quyền
- Xóa file cũ định kỳ

### 5. Kiểm Tra Định Kỳ

**Mỗi tháng:**
1. Export Excel
2. Mở file kiểm tra
3. So sánh với tháng trước
4. Phát hiện xu hướng vi phạm
5. Lập kế hoạch cải thiện

## 🎨 Tùy Chỉnh

### Thêm Sheet Mới

Muốn thêm sheet "Overtime"?

**Bước 1:** Tạo method trong `ExcelExportService`:
```python
@staticmethod
def _create_overtime_sheet(wb: Workbook, session):
    ws = wb.create_sheet("Overtime")
    # ... custom logic
```

**Bước 2:** Gọi trong `create_backup_excel()`:
```python
ExcelExportService._create_overtime_sheet(wb, session)
```

### Thay Đổi Màu Sắc

Trong mỗi `_create_*_sheet()` method:
```python
header_fill = PatternFill(
    start_color="YOUR_HEX_COLOR",
    end_color="YOUR_HEX_COLOR",
    fill_type="solid"
)
```

### Thêm Biểu Đồ

```python
from openpyxl.chart import BarChart, Reference

chart = BarChart()
data = Reference(ws, min_col=2, min_row=1, max_row=10)
chart.add_data(data, titles_from_data=True)
ws.add_chart(chart, "E5")
```

## 📞 Troubleshooting

### File quá lớn (> 8MB)?

**Discord giới hạn:** 8MB cho file upload

**Giải pháp:**
1. Export riêng từng tháng
2. Nén file (zip)
3. Upload lên cloud, gửi link

### Lỗi "openpyxl not found"?

```bash
pip install openpyxl
```

### File bị lỗi khi mở?

**Nguyên nhân:** Export chưa hoàn tất

**Giải pháp:**
- Đợi bot response "✅ Đã xuất dữ liệu thành công"
- Không tắt bot giữa chừng
- Kiểm tra thư mục `backups/`

### Dữ liệu thiếu?

**Kiểm tra:**
1. Database có dữ liệu không?
   ```sql
   SELECT COUNT(*) FROM attendances;
   ```
2. Sheet có bị ẩn không?
3. Filter có đang bật không?

## 🔮 Tính Năng Tương Lai

- [ ] Export theo khoảng thời gian tùy chỉnh
- [ ] Export chỉ một user cụ thể
- [ ] Thêm biểu đồ tự động
- [ ] Export PDF
- [ ] Schedule auto-export hàng tháng
- [ ] Email file Excel tự động
- [ ] Integrate với Google Sheets
- [ ] Template tùy chỉnh

## 📊 Ví Dụ Thực Tế

### Scenario: Báo Cáo Tháng 10/2025

**Bước 1:** Export dữ liệu
```
/admin export
```

**Bước 2:** Mở file Excel

**Bước 3:** Xem "Tóm Tắt"
- Tổng 450 lần chấm công
- 89 lần nghỉ giải lao
- 25 lần quên chấm công
- 12 vi phạm làm thiếu giờ

**Bước 4:** Xem "Chấm Công"
- Dòng vàng: 12 người vi phạm < 8h
- Lọc theo user cụ thể
- Tính trung bình giờ làm

**Bước 5:** Tạo PivotTable
- Tổng giờ làm theo tuần
- So sánh performance giữa các team

**Bước 6:** Gửi báo cáo cho quản lý
- File Excel đã format đẹp
- Kèm phân tích
- Đề xuất cải thiện

---

## 🎉 Tóm Tắt

✅ Command mới: `/admin export`
✅ 6 sheets chi tiết với màu sắc đẹp mắt
✅ Tự động format, tính toán
✅ Highlight vi phạm
✅ Top performers
✅ Dễ chia sẻ và phân tích
✅ Tương thích với Excel, Google Sheets

**Version:** 4.0  
**Updated:** 2025-10-09  
**Status:** ✅ Production Ready
