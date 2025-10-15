# 📋 Hệ Thống Ghi Log Vi Phạm

## 🎯 Tổng Quan

Hệ thống tự động phát hiện, ghi log và thông báo các vi phạm chấm công của nhân viên.

## 🔍 Các Loại Vi Phạm

### 1. ❌ Quên Check-in
- **Mô tả**: Nhân viên không thực hiện check-in trong suốt ngày làm việc
- **Mức độ**: ⚡ Warning (Cảnh báo)
- **Hành động**: Ghi log + Gửi DM nhắc nhở

### 2. ⚠️ Quên Check-out
- **Mô tả**: Nhân viên đã check-in nhưng quên check-out
- **Mức độ**: ⚡ Warning (Cảnh báo)
- **Hành động**: Ghi log + Gửi DM nhắc nhở

### 3. 🚨 Làm Thiếu Giờ
- **Mô tả**: Nhân viên làm việc ít hơn 8 giờ/ngày (28800 giây)
- **Mức độ**: 🔥 Error (Nghiêm trọng)
- **Hành động**: Ghi log + Gửi DM cảnh báo + Yêu cầu giải trình

## 📊 Cách Hoạt Động

### Tự Động Ghi Log Khi Xem Báo Cáo

Khi Admin/Owner sử dụng lệnh `/report daily`, hệ thống sẽ:

1. ✅ **Phân tích** tất cả attendance trong ngày
2. ✅ **Phát hiện** các vi phạm (quên check-in, quên check-out, thiếu giờ)
3. ✅ **Ghi log** vào kênh **log-vi-phạm**
4. ✅ **Gửi DM** thông báo cho người vi phạm

### Kiểm Tra Thủ Công

Admin có thể chủ động kiểm tra vi phạm:

```
/report violations [date]
```

**Tham số:**
- `date`: Ngày cần kiểm tra (YYYY-MM-DD), mặc định là hôm nay

**Ví dụ:**
```
/report violations 2025-10-09
/report violations
```

**Kết quả:**
- ✅ Ghi log tất cả vi phạm vào kênh **log-vi-phạm**
- ✅ Gửi tóm tắt vi phạm vào kênh **thông-báo**
- ✅ Gửi DM thông báo cho từng người vi phạm

## 📝 Chi Tiết Log Vi Phạm

### Format Embed trong kênh log-vi-phạm

**Title:** 🚨 [Loại Vi Phạm]

**Thông tin:**
- 👤 **Người vi phạm**: @mention + username
- 📋 **Chi Tiết Vi Phạm**: 
  - Ngày vi phạm
  - Thời gian check-in/out (nếu có)
  - Số giờ làm việc thực tế
  - Số giờ thiếu (đối với vi phạm thiếu giờ)
- 🔴 **Mức Độ**: WARNING / ERROR / CRITICAL
- 🆔 **User ID**: ID Discord của người vi phạm
- 🕐 **Timestamp**: Thời gian ghi nhận vi phạm

### Ví Dụ Log

#### Vi Phạm Quên Check-in:
```
⚡ Quên Check-in

Người vi phạm: @JohnDoe (JohnDoe#1234)

📋 Chi Tiết Vi Phạm
Ngày: 2025-10-09
Người dùng không thực hiện check-in trong suốt ngày làm việc.

🔴 Mức Độ
WARNING

🆔 User ID
123456789012345678
```

#### Vi Phạm Làm Thiếu Giờ:
```
🚨 Làm Thiếu Giờ

Người vi phạm: @JaneDoe (JaneDoe#5678)

📋 Chi Tiết Vi Phạm
Ngày: 2025-10-09
Check-in: 09:00:00
Check-out: 16:30:00
Thời gian làm việc: 7h 30m
Thiếu: ~0.5h so với quy định 8h/ngày

🔴 Mức Độ
ERROR

🆔 User ID
987654321098765432
```

## 📬 Thông Báo DM Cho Người Vi Phạm

Nhân viên vi phạm sẽ nhận được DM với nội dung:

### Quên Check-in:
```
⚠️ Bạn Quên Check-in

Bạn chưa check-in vào ngày 2025-10-09. Vui lòng liên hệ Admin để bổ sung.

💡 Khuyến Nghị
• Hãy chấm công đầy đủ và đúng giờ
• Liên hệ Admin nếu có sự cố
• Dùng /manual để bổ sung nếu quên
```

### Làm Thiếu Giờ:
```
🚨 Bạn Làm Thiếu Giờ

Bạn chỉ làm 7h 30m vào ngày 2025-10-09.
Thiếu ~0.5h so với quy định 8h/ngày.
Vui lòng giải trình với Admin.

💡 Khuyến Nghị
• Hãy chấm công đầy đủ và đúng giờ
• Liên hệ Admin nếu có sự cố
• Dùng /manual để bổ sung nếu quên
```

## 📊 Tóm Tắt Vi Phạm (Kênh thông-báo)

Khi có vi phạm, Admin sẽ nhận được tóm tắt:

```
📊 Tóm Tắt Vi Phạm Ngày 2025-10-09

Tổng số vi phạm: 15 lượt

❌ Quên Check-in
5 người

⚠️ Quên Check-out
4 người

🚨 Làm Thiếu Giờ
6 người

📋 Chi Tiết
Xem chi tiết trong kênh log-vi-phạm
```

## 🔧 Cấu Hình Kênh

### Kênh log-vi-phạm
- **Tên**: `log-vi-phạm`
- **Loại**: Text Channel
- **Quyền**: Chỉ Admin/Owner xem được
- **Tự động tạo**: Nếu chưa có, bot sẽ tự tạo khi ghi log lần đầu

### Kênh thông-báo
- **Tên**: `thông-báo`
- **Loại**: Text Channel
- **Mục đích**: Nhận tóm tắt vi phạm hàng ngày

## 📈 Workflow Hoàn Chỉnh

```
1. Admin chạy /report daily [date]
   ↓
2. Bot phân tích attendance
   ↓
3. Phát hiện vi phạm
   ↓
4. Ghi log vào log-vi-phạm (cho mỗi người)
   ↓
5. Gửi DM cho người vi phạm
   ↓
6. (Nếu dùng /report violations) Gửi tóm tắt vào thông-báo
```

## ⚙️ Code API

### ViolationLogger Class

```python
from services.violation_logger import ViolationLogger, ViolationType

# Khởi tạo
logger = ViolationLogger(bot)

# Ghi log vi phạm
await logger.log_violation(
    guild=guild,
    user=user,
    violation_type=ViolationType.INSUFFICIENT_HOURS,
    details="Chi tiết vi phạm...",
    severity="error"  # "warning", "error", "critical"
)

# Gửi thông báo
await logger.send_violation_notification(
    user=user,
    violation_type=ViolationType.FORGOT_CHECKOUT,
    details="Chi tiết...",
    send_dm=True
)

# Kiểm tra vi phạm của một ngày
await logger.check_and_log_violations(guild, "2025-10-09")

# Gửi tóm tắt cho admin
await logger.notify_admin_summary(guild, "2025-10-09")
```

### ViolationType Constants

```python
ViolationType.FORGOT_CHECKIN       # Quên check-in
ViolationType.FORGOT_CHECKOUT      # Quên check-out
ViolationType.INSUFFICIENT_HOURS   # Làm thiếu giờ
ViolationType.LATE_ARRIVAL         # Đi làm muộn (chưa dùng)
ViolationType.EARLY_DEPARTURE      # Về sớm (chưa dùng)
```

## 🎨 Màu Sắc Theo Mức Độ

- 🟡 **Warning**: Màu vàng (discord.Color.yellow())
- 🟠 **Error**: Màu cam (discord.Color.orange())
- 🔴 **Critical**: Màu đỏ (discord.Color.red())

## 📌 Lưu Ý

1. ✅ Log vi phạm tự động kích hoạt khi chạy `/report daily`
2. ✅ DM có thể bị chặn nếu user tắt nhận DM từ bot
3. ✅ Kênh log-vi-phạm nên set quyền chỉ Admin xem được
4. ✅ Vi phạm được ghi nhận theo múi giờ hệ thống
5. ✅ Threshold thiếu giờ: < 8 giờ = 28800 giây

## 🔮 Tính Năng Tương Lai

- [ ] Tự động kiểm tra vi phạm vào cuối ngày (scheduled task)
- [ ] Gửi báo cáo tuần cho Owner về top violators
- [ ] Hệ thống điểm phạt tích lũy
- [ ] Export vi phạm ra Excel
- [ ] Dashboard thống kê vi phạm theo tháng
