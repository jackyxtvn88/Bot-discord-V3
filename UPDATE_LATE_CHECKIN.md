# 🆕 Cập Nhật: Hệ Thống Vi Phạm Chấm Công Muộn

## ✨ Tính Năng Mới

### ⏰ Phát Hiện và Ghi Log Chấm Công Muộn

Bot giờ đây tự động phát hiện và ghi log khi nhân viên:
1. **Check-in muộn** - Chấm công sau giờ bắt đầu làm việc đã set
2. **Check-out muộn** - Check-out sau giờ kết thúc làm việc đã set

## 🔍 Cách Hoạt Động

### 1. Khi Check-in Muộn

**Ngay khi check-in:**
- ✅ Nhân viên nhận thông báo: `⚠️ Bạn đã đi trễ X phút so với giờ quy định (HH:MM)`
- 📝 **Tự động ghi log** vào kênh **log-vi-phạm**:
  ```
  ⏰ Chấm Công Muộn
  
  Người vi phạm: @User
  
  📋 Chi Tiết Vi Phạm
  Ngày: 2025-10-09
  Giờ quy định: 08:00
  Giờ check-in thực tế: 08:45:00
  Muộn: 45 phút
  
  🔴 Mức Độ: WARNING
  ```

### 2. Khi Check-out Quá Giờ

**Khi check-out muộn:**
- ✅ Nhân viên nhận thông báo: `⚠️ Bạn đã check-out muộn X phút so với giờ quy định (HH:MM)`
- 📝 **Tự động ghi log** vào kênh **log-vi-phạm**:
  ```
  ⏰ Check-out Muộn
  
  Người vi phạm: @User
  
  📋 Chi Tiết Vi Phạm
  Ngày: 2025-10-09
  Giờ quy định: 17:00
  Giờ check-out thực tế: 18:30:00
  Muộn: 90 phút
  Tổng giờ làm: 9h 45m
  
  🔴 Mức Độ: WARNING
  ```

### 3. Trong Báo Cáo

#### `/report daily [date]`
**Mục mới hiển thị:**
```
⏰ Chấm Công Muộn (5 người)
User1 (muộn 15p)
User2 (muộn 30p)
User3 (muộn 10p)
User4 (muộn 45p)
User5 (muộn 20p)
```

#### `/report weekly [start_date]`
**Mục mới hiển thị:**
```
⏰ Top Chấm Muộn (10 người)
User1: 3 lần
User2: 2 lần
User3: 2 lần
...
```

#### `/report monthly [year] [month]`
**Mục mới hiển thị:**
```
⏰ Top Chấm Muộn (15 người)
**User1**: 8 lần
**User2**: 6 lần
**User3**: 5 lần
...
```

## 🛠️ Cấu Hình Thời Gian Làm Việc

Để hệ thống hoạt động, Admin cần set thời gian làm việc:

### Set cho cả Server (mặc định cho tất cả)
```
/worktime set start_time:08:00 end_time:17:00
```

### Set riêng cho từng người
```
/worktime set user:@User start_time:09:00 end_time:18:00
```

### Xem thời gian làm việc hiện tại
```
/worktime view [user]
```

## 📊 Chi Tiết Kỹ Thuật

### Cách Tính Chấm Muộn

**Check-in muộn:**
- So sánh thời gian check-in thực tế với `start_time` đã set
- Nếu check-in > start_time → Ghi nhận vi phạm
- Tính số phút muộn: `(check-in time - start time) in minutes`

**Check-out muộn:**
- So sánh thời gian check-out thực tế với `end_time` đã set
- Nếu check-out > end_time → Ghi nhận vi phạm
- Tính số phút muộn: `(check-out time - end time) in minutes`

### Functions Mới

**work_time_service.py:**
```python
# Kiểm tra có chấm muộn không
is_late, mins_late = work_time_service.is_late_checkin(user_id, "08:45:00")
# Returns: (True, 45) nếu giờ quy định là 08:00

# Kiểm tra đã quá giờ làm việc chưa
is_past = work_time_service.is_past_work_time(user_id)
# Returns: True nếu hiện tại > end_time
```

**ViolationType constants:**
```python
ViolationType.LATE_CHECKIN   # Chấm công muộn
ViolationType.LATE_CHECKOUT  # Check-out muộn
```

## 🎯 Ví Dụ Sử Dụng

### Scenario 1: Nhân viên đi trễ 30 phút

1. **Giờ quy định:** 08:00 - 17:00
2. **Thực tế:** Check-in lúc 08:30

**Kết quả:**
- ✅ Check-in thành công
- ⚠️ Thông báo: "Bạn đã đi trễ 30 phút"
- 📝 Ghi log tự động vào **log-vi-phạm**
- 📊 Hiển thị trong `/report daily`

### Scenario 2: Nhân viên làm overtime

1. **Giờ quy định:** 08:00 - 17:00
2. **Thực tế:** Check-in 08:00, Check-out 19:00

**Kết quả:**
- ✅ Check-out thành công
- ⚠️ Thông báo: "Bạn đã check-out muộn 120 phút"
- 📝 Ghi log tự động vào **log-vi-phạm**
- ℹ️ **Note:** Đây có thể là overtime hợp lệ, Admin nên kiểm tra

## 📋 Files Đã Cập Nhật

### 1. **services/violation_logger.py**
- Thêm `ViolationType.LATE_CHECKIN`
- Thêm `ViolationType.LATE_CHECKOUT`
- Cập nhật titles và thông báo

### 2. **services/work_time_service.py**
- Thêm function `is_late_checkin(user_id, checkin_time_str)`
- Thêm function `is_past_work_time(user_id)`
- Logic tính toán số phút muộn

### 3. **cogs/attendance.py**
- Tích hợp `ViolationLogger`
- Ghi log khi check-in muộn (sau start_time)
- Ghi log khi check-out muộn (sau end_time)
- Hiển thị cảnh báo cho user

### 4. **cogs/reports.py**
- Import `work_time_service`
- Thêm phát hiện vi phạm chấm muộn trong `daily_report`
- Thêm field "⏰ Chấm Công Muộn" với danh sách + số phút muộn
- Thêm `late_checkin_count` trong `weekly_report` (Top 10)
- Thêm `late_checkin_stats` trong `monthly_report` (Top 10)

## ⚙️ Cấu Hình Khuyến Nghị

### 1. Thiết Lập Thời Gian Mặc Định
```
/worktime set start_time:08:00 end_time:17:00 break_min:30 break_max:60
```

### 2. Tạo Kênh Log (nếu chưa có)
- Tên: `log-vi-phạm`
- Quyền: Chỉ Admin/Owner xem được
- Bot tự tạo nếu chưa có

### 3. Kiểm Tra Thường Xuyên
```
/report daily          # Xem vi phạm hôm nay
/report weekly         # Xem xu hướng tuần
/report monthly        # Xem tổng quan tháng
```

## 🚨 Lưu Ý Quan Trọng

1. ⚠️ **Check-out muộn** không phải lúc nào cũng là vi phạm:
   - Có thể là làm overtime hợp lệ
   - Admin nên xem xét từng trường hợp
   - Có thể whitelist nếu cần

2. ⚠️ **Múi giờ**: 
   - Bot sử dụng múi giờ hệ thống
   - Đảm bảo server time chính xác

3. ⚠️ **Work Time chưa set**:
   - Nếu user chưa có work_time → Không kiểm tra vi phạm
   - Khuyến nghị: Set default work_time cho cả server

## 🎨 Giao Diện Log

### Log Format

```
[Emoji] [Title]

Người vi phạm: @User (Username#1234)

📋 Chi Tiết Vi Phạm
[Chi tiết cụ thể]

🔴 Mức Độ
WARNING / ERROR / CRITICAL

🆔 User ID
123456789012345678

⏰ [Timestamp]
Vi phạm được ghi nhận tự động
```

### Màu Sắc
- 🟡 **Chấm muộn:** Màu vàng (Warning)
- 🟠 **Làm thiếu giờ:** Màu cam (Error)
- 🔴 **Vi phạm nghiêm trọng:** Màu đỏ (Critical)

## 📈 Workflow Tổng Quan

```
User check-in/out
    ↓
Bot kiểm tra work_time
    ↓
Nếu muộn → Ghi log ngay lập tức
    ↓
Log xuất hiện trong log-vi-phạm
    ↓
Admin xem báo cáo daily/weekly/monthly
    ↓
Thấy thống kê vi phạm chấm muộn
    ↓
Xử lý theo quy định công ty
```

## 🔮 Tính Năng Có Thể Mở Rộng

- [ ] Cho phép "grace period" (chấm muộn dưới 5 phút = OK)
- [ ] Whitelist overtime cho một số người
- [ ] Gửi cảnh báo tự động khi chấm muộn quá X lần/tháng
- [ ] Dashboard thống kê tỷ lệ chấm muộn theo tháng
- [ ] Tích hợp với hệ thống đánh giá nhân viên

## 📞 Hỗ Trợ

Nếu có vấn đề:
1. Kiểm tra `/worktime view` xem đã set thời gian chưa
2. Xem log trong **log-vi-phạm** để debug
3. Test với `/report daily` để xem có hoạt động không

---

**Version:** 2.0
**Updated:** 2025-10-09
**Status:** ✅ Production Ready
