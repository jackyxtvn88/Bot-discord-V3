# 🔔 Hệ Thống Cảnh Báo Tự Động

## ✨ Tổng Quan

Bot giờ đây có **hệ thống giám sát tự động 24/7** để cảnh báo nhân viên khi:
1. ⏰ **Quá 15 phút** kể từ giờ bắt đầu làm việc mà chưa check-in
2. ⏰ **Quá 1 tiếng** kể từ giờ kết thúc làm việc mà chưa check-out

## 🚨 Cách Hoạt Động

### 1. Cảnh Báo Chưa Check-in (15 phút)

**Kịch bản:**
- Giờ làm việc: 08:00 - 17:00
- Đã 08:15 mà user chưa check-in

**Hành động tự động:**
1. ✅ Bot gửi **DM** cho user:
   ```
   ⚠️ CẢNH BÁO: Chưa Check-in
   
   Bạn chưa check-in hôm nay!
   
   Giờ quy định: 08:00
   Thời gian hiện tại: 08:15:00
   Bạn đã trễ: 15 phút
   
   ⚡ Vui lòng check-in ngay hoặc liên hệ Admin nếu có lý do chính đáng!
   ```

2. ✅ Bot gửi thông báo vào kênh **thông-báo**:
   ```
   ⚠️ @User chưa check-in sau 15 phút kể từ giờ quy định!
   ```

3. ✅ Bot ghi log vào kênh **log-vi-phạm**:
   ```
   ❌ Quên Check-in
   
   Người vi phạm: @User
   
   📋 Chi Tiết Vi Phạm
   Ngày: 2025-10-09
   Giờ quy định: 08:00
   Thời gian kiểm tra: 08:15:00
   Đã trễ: 15 phút
   ⚠️ Cảnh báo tự động sau 15 phút
   ```

### 2. Cảnh Báo Chưa Check-out (1 tiếng)

**Kịch bản:**
- Giờ làm việc: 08:00 - 17:00
- User đã check-in lúc 08:00
- Đã 18:00 (quá 1 tiếng) mà chưa check-out

**Hành động tự động:**
1. ✅ Bot gửi **DM** cho user:
   ```
   ⚠️ CẢNH BÁO: Chưa Check-out
   
   Bạn chưa check-out hôm nay!
   
   Check-in lúc: 08:00:00
   Giờ kết thúc quy định: 17:00
   Thời gian hiện tại: 18:00:00
   Quá giờ: 60 phút
   Đã làm việc: 10h 0m
   
   ⚡ Vui lòng check-out ngay để kết thúc ca làm việc!
   ```

2. ✅ Bot gửi thông báo vào kênh **thông-báo**
3. ✅ Bot ghi log vào kênh **log-vi-phạm**

## ⚙️ Cấu Hình

### Xem Cấu Hình Hiện Tại

```
/admin warning
```

**Kết quả:**
```
⚙️ Cấu Hình Cảnh Báo Tự Động

⏰ Check-in Grace Period
15 phút
Cảnh báo sau 15 phút kể từ giờ bắt đầu làm việc

⏰ Check-out Grace Period
60 phút
Cảnh báo sau 60 phút kể từ giờ kết thúc làm việc

📊 Trạng Thái
✅ Đang hoạt động
```

### Thay Đổi Cấu Hình

**Thay đổi grace period check-in:**
```
/admin warning checkin_grace:30
```
→ Cảnh báo sau **30 phút** thay vì 15 phút

**Thay đổi grace period check-out:**
```
/admin warning checkout_grace:120
```
→ Cảnh báo sau **2 tiếng** thay vì 1 tiếng

**Thay đổi cả hai:**
```
/admin warning checkin_grace:20 checkout_grace:90
```

**Giới hạn:**
- Check-in grace: **1-120 phút**
- Check-out grace: **1-240 phút** (4 tiếng)

## 📊 Quy Trình Giám Sát

```
Bot khởi động
    ↓
Bắt đầu 3 tasks:
    ├─ check_late_checkin (mỗi 5 phút)
    ├─ check_late_checkout (mỗi 5 phút)
    └─ reset_daily_warnings (mỗi 24 giờ)
    ↓
Mỗi 5 phút bot kiểm tra:
    ├─ Lấy tất cả work_time settings
    ├─ Kiểm tra từng user
    ├─ So sánh với attendance
    └─ Gửi cảnh báo nếu vi phạm
    ↓
Ghi nhớ đã cảnh báo (không spam)
    ↓
Reset danh sách mỗi ngày
```

## 🎯 Ví Dụ Thực Tế

### Scenario 1: Nhân viên quên check-in

**Timeline:**
- 08:00 - Giờ bắt đầu (không check-in)
- 08:05 - Bot kiểm tra lần 1 (chưa đủ 15 phút)
- 08:10 - Bot kiểm tra lần 2 (chưa đủ 15 phút)
- 08:15 - Bot kiểm tra lần 3 → **CẢNH BÁO**
  - Gửi DM cho user
  - Gửi thông báo vào thông-báo
  - Ghi log vào log-vi-phạm
- 08:20 - Bot kiểm tra lần 4 (đã cảnh báo rồi, bỏ qua)
- 08:25 - User check-in muộn
- 08:30 - Bot kiểm tra, thấy đã check-in, bỏ qua

### Scenario 2: Nhân viên làm overtime quên check-out

**Timeline:**
- 08:00 - User check-in
- 17:00 - Giờ kết thúc (user tiếp tục làm, quên check-out)
- 17:30 - Bot kiểm tra (chưa đủ 1 tiếng)
- 18:00 - Bot kiểm tra (chưa đủ 1 tiếng)
- 18:05 - Bot kiểm tra → **CẢNH BÁO**
  - Gửi DM: "Bạn đã làm 10h 5m, vui lòng check-out"
  - Gửi thông báo
  - Ghi log
- 18:10 - User check-out

## 🔧 Chi Tiết Kỹ Thuật

### AutoWarningService

**File:** `services/auto_warning_service.py`

**Constants:**
```python
CHECKIN_GRACE_MINUTES = 15   # Mặc định 15 phút
CHECKOUT_GRACE_MINUTES = 60  # Mặc định 60 phút
```

**Tasks:**
```python
@tasks.loop(minutes=5)
async def check_late_checkin():
    # Kiểm tra mỗi 5 phút
    # Lấy tất cả work_time
    # So sánh với attendance
    # Gửi cảnh báo nếu quá grace period

@tasks.loop(minutes=5)
async def check_late_checkout():
    # Tương tự check_late_checkin
    # Nhưng check những người đã check-in mà chưa check-out

@tasks.loop(hours=24)
async def reset_daily_warnings():
    # Reset danh sách đã cảnh báo mỗi ngày
    # Tránh spam cảnh báo
```

**Anti-spam:**
```python
self.warned_users_checkin = set()   # {user_id_date_checkin}
self.warned_users_checkout = set()  # {user_id_date_checkout}
```

Mỗi user chỉ nhận **1 cảnh báo/ngày** cho mỗi loại vi phạm.

### Integration với Main Bot

**main.py:**
```python
class AttendanceBot(commands.Bot):
    def __init__(self):
        ...
        self.auto_warning_service = None
    
    async def setup_hook(self):
        ...
        self.auto_warning_service = AutoWarningService(self)
    
    async def on_ready(self):
        ...
        self.auto_warning_service.start_monitoring()
```

## 📋 Yêu Cầu

### 1. Work Time Phải Được Set

Bot chỉ giám sát những user đã có `work_time` setting:

```python
# Kiểm tra trong database
SELECT * FROM work_times WHERE user_id = '123456789';
```

**Nếu chưa có:** Sử dụng `/worktime set` để thiết lập

### 2. Kênh Cần Thiết

- **thông-báo**: Nhận cảnh báo công khai
- **log-vi-phạm**: Nhận log chi tiết

Bot tự tạo nếu chưa có.

## 🚦 Workflow Cảnh Báo

```
[Mỗi 5 phút]
    ↓
Kiểm tra thời gian hiện tại
    ↓
Lấy danh sách work_time
    ↓
Với mỗi user:
    ├─ Tính warning_time = start_time + grace_minutes
    ├─ Nếu current_time > warning_time:
    │   ├─ Kiểm tra attendance
    │   ├─ Nếu chưa check-in và chưa cảnh báo:
    │   │   ├─ Gửi DM
    │   │   ├─ Gửi thông-báo
    │   │   ├─ Ghi log-vi-phạm
    │   │   └─ Đánh dấu đã cảnh báo
    │   └─ Bỏ qua nếu đã cảnh báo
    └─ Bỏ qua nếu chưa đến warning_time
```

## 💡 Tips & Best Practices

### 1. Thiết Lập Grace Period Hợp Lý

**Check-in:**
- 5-10 phút: Rất nghiêm ngặt
- 15-20 phút: **Khuyến nghị** (mặc định 15)
- 30+ phút: Quá lỏng lẻo

**Check-out:**
- 30 phút: Nghiêm ngặt với overtime
- 60 phút: **Khuyến nghị** (mặc định 60)
- 120+ phút: Cho phép overtime nhiều

### 2. Xử Lý Trường Hợp Đặc Biệt

**Nhân viên remote/flexible:**
```
/worktime set user:@RemoteWorker start_time:09:00 end_time:18:00
```

**Nhân viên ca đêm:**
```
/worktime set user:@NightShift start_time:22:00 end_time:06:00
```

**Disable monitoring cho user:**
Xóa work_time setting của user đó.

### 3. Giám Sát Hiệu Quả

**Hàng ngày:**
- Xem kênh **thông-báo** để biết ai được cảnh báo
- Xem kênh **log-vi-phạm** để có chi tiết

**Hàng tuần:**
```
/report weekly
```
Xem top người vi phạm nhiều nhất

**Hàng tháng:**
```
/report monthly
```
Phân tích xu hướng vi phạm

## 🔮 Tính Năng Có Thể Mở Rộng

- [ ] Cảnh báo lặp lại (mỗi 30 phút cho đến khi check-in)
- [ ] Escalation (cảnh báo Admin sau 2 tiếng)
- [ ] Whitelist ngày (không cảnh báo vào ngày nghỉ)
- [ ] SMS/Email notification
- [ ] Dashboard real-time
- [ ] Machine learning dự đoán vi phạm

## 📞 Troubleshooting

### Bot không gửi cảnh báo?

**Kiểm tra:**
1. Bot đã khởi động đầy đủ?
   ```
   Logged in as XTVN88#5375
   Auto warning monitoring started!
   - Check-in grace period: 15 minutes
   - Check-out grace period: 60 minutes
   ```

2. User có work_time setting?
   ```
   /worktime view user:@User
   ```

3. Đã quá grace period?
   - Hiện tại > start_time + 15 phút?
   - Hiện tại > end_time + 60 phút?

4. Đã cảnh báo rồi?
   - Bot chỉ cảnh báo 1 lần/ngày/user

### Bot gửi cảnh báo spam?

**Không thể xảy ra** - Bot có anti-spam built-in:
```python
if warning_key not in self.warned_users_checkin:
    # Chỉ gửi nếu chưa cảnh báo
    await self._send_late_checkin_warning(...)
    self.warned_users_checkin.add(warning_key)
```

### User không nhận DM?

**Nguyên nhân:** User đã tắt DM từ bot

**Giải pháp:** Vẫn có cảnh báo trong kênh **thông-báo**

## 📊 Logs & Monitoring

### Xem Log Bot

```powershell
# Terminal output
2025-10-09 17:30:34 INFO discord Auto warning monitoring started!
2025-10-09 17:30:34 INFO discord   - Check-in grace period: 15 minutes
2025-10-09 17:30:34 INFO discord   - Check-out grace period: 60 minutes
```

### Kiểm Tra Trạng Thái

```
/admin warning
```

### Xem Lịch Sử Cảnh Báo

Trong kênh **log-vi-phạm**, tìm:
```
⚠️ Cảnh báo tự động sau 15 phút
⚠️ Cảnh báo tự động sau 60 phút
```

---

## 🎉 Tóm Tắt

✅ Bot giờ giám sát **tự động 24/7**
✅ Cảnh báo **15 phút** chưa check-in (có thể thay đổi)
✅ Cảnh báo **60 phút** chưa check-out (có thể thay đổi)
✅ Gửi **DM + Thông báo + Log** đầy đủ
✅ **Anti-spam** - chỉ 1 cảnh báo/ngày/user
✅ **Tự động reset** mỗi ngày
✅ **Dễ cấu hình** với `/admin warning`

**Version:** 3.0  
**Updated:** 2025-10-09  
**Status:** ✅ Production Ready
