# 🤖 Discord HR Bot - Hệ Thống Chấm Công Tự Động

Bot Discord chuyên nghiệp cho quản lý chấm công, theo dõi thời gian làm việc và báo cáo tự động.

## ✨ Tính Năng Chính

### 📋 Quản Lý Chấm Công
- ✅ Check-in/Check-out tự động
- 🍵 Quản lý giờ nghỉ giải lao
- ⏱️ Tính toán tổng giờ làm việc
- 📊 Báo cáo chi tiết (ngày/tuần/tháng)
- 📝 Chấm công thủ công (cho admin)

### ⚠️ Phát Hiện Vi Phạm
- 🚨 Tự động phát hiện đi muộn (> 15 phút)
- 🚨 Phát hiện về muộn (> 60 phút)
- 📉 Phát hiện làm thiếu giờ (< 8 giờ)
- ❌ Theo dõi quên check-in/out
- 📨 Cảnh báo tự động qua DM
- 📋 Ghi log vi phạm vào kênh chuyên dụng

### 📊 Báo Cáo & Xuất Dữ Liệu
- 📈 Báo cáo hàng ngày/tuần/tháng
- 🏆 Xếp hạng top performers
- 📊 Thống kê vi phạm chi tiết
- 📁 Backup database (.db)
- 📊 **Xuất Excel chi tiết với 6 sheets**

### 🎯 Quản Lý Nâng Cao
- ⏰ Cấu hình giờ làm việc linh hoạt
- 🏖️ Đăng ký ngày nghỉ
- 👥 Quản lý theo nhóm/cá nhân
- 🔒 Phân quyền rõ ràng (Owner/Admin/Member)
- 🎨 Giao diện lịch tương tác

## 📦 Cài Đặt

### Yêu Cầu Hệ Thống
- Python 3.11+
- Discord Bot Token
- SQLite (đã bao gồm)

### Các Bước Cài Đặt

**1. Clone repository:**
```bash
git clone <repository-url>
cd "code diem danh discord"
```

**2. Tạo môi trường ảo:**
```bash
python -m venv .venv
```

**3. Kích hoạt môi trường ảo:**

Windows:
```bash
.venv\Scripts\activate
```

Linux/Mac:
```bash
source .venv/bin/activate
```

**4. Cài đặt dependencies:**
```bash
pip install -r requirements.txt
```

**5. Cấu hình bot:**

Tạo file `.env`:
```env
DISCORD_TOKEN=your_bot_token_here
```

**6. Khởi tạo database:**
```bash
python init_db.py
```

**7. Chạy bot:**
```bash
python main.py
```

## 📚 Dependencies

```txt
discord.py>=2.0.0
sqlalchemy>=2.0.0
python-dotenv>=1.0.0
openpyxl>=3.1.0
```

## 🎮 Hướng Dẫn Sử Dụng

### 🔰 Lệnh Cơ Bản (Cho Tất Cả Members)

#### Check-in/Check-out
```
/checkin          - Chấm công vào
/checkout         - Chấm công ra
/breakstart       - Bắt đầu nghỉ giải lao
/breakend         - Kết thúc nghỉ giải lao
```

#### Xem Thông Tin
```
/menu             - Menu chính với các nút tương tác
/thongtin         - Xem thông tin chấm công của bạn
/worktime view    - Xem cấu hình giờ làm việc
```

### 👑 Lệnh Admin

#### Quản Lý Chấm Công
```
/manual addcheckin [user] [date] [time] [reason]
  - Thêm check-in thủ công
  
/manual addcheckout [user] [date] [time] [reason]
  - Thêm check-out thủ công
  
/manual forgot [user] [date] [type] [reason]
  - Đánh dấu quên chấm công
```

#### Cấu Hình Hệ Thống
```
/admin setdefaultworktime [start] [end] [break_min] [break_max]
  - Thiết lập giờ làm việc mặc định cho server
  
/admin setworktime [user] [start] [end] [break_min] [break_max]
  - Thiết lập giờ làm việc riêng cho user
  
/admin warning [checkin_grace] [checkout_grace]
  - Cấu hình thời gian grace cho cảnh báo
```

#### Quản Lý Ngày Nghỉ
```
/dayoff add [date] [reason]
  - Đăng ký ngày nghỉ cho toàn server
  
/dayoff list
  - Xem danh sách ngày nghỉ
  
/dayoff remove [date]
  - Xóa ngày nghỉ
```

#### Báo Cáo
```
/report daily [date]
  - Báo cáo chấm công trong ngày
  
/report weekly [start_date]
  - Báo cáo tuần
  
/report monthly [month] [year]
  - Báo cáo tháng
```

#### Backup & Export
```
/admin backup
  - Backup database (.db file)
  
/admin export
  - Xuất dữ liệu ra Excel chi tiết
  
/admin restore [backup_file]
  - Khôi phục từ backup
```

#### Quản Lý Dữ Liệu
```
/admin reset [user] [date]
  - Reset dữ liệu chấm công
  
/admin delete [user] [date]
  - Xóa dữ liệu chấm công
```

### 📊 Lệnh Xuất Excel (MỚI!)

```
/admin export
```

**File Excel bao gồm 6 sheets:**

1. **📊 Tóm Tắt** - Overview và Top 5
2. **✅ Chấm Công** - Chi tiết attendance (có highlight vi phạm)
3. **🍵 Nghỉ Giải Lao** - Break sessions
4. **⏰ Thời Gian Làm Việc** - Work time configs
5. **❌ Quên Chấm Công** - Forgot records
6. **🏖️ Ngày Nghỉ** - Day offs

**Định dạng:**
- ✨ Professional styling với màu sắc
- 🟨 Highlight vàng cho vi phạm
- 📊 Tự động tính toán
- 📏 Auto column width

## 🏗️ Cấu Trúc Dự Án

```
code diem danh discord/
├── main.py                      # Entry point
├── init_db.py                   # Database initialization
├── database.py                  # Database connection
├── models.py                    # SQLAlchemy models
├── requirements.txt             # Dependencies
├── .env                         # Environment variables
├── attendance.db                # SQLite database
├── cogs/                        # Discord cogs
│   ├── attendance.py           # Check-in/out commands
│   ├── admin.py                # Admin commands
│   ├── reports.py              # Báo cáo
│   ├── manual_attendance.py    # Chấm công thủ công
│   ├── dayoff_manager.py       # Quản lý ngày nghỉ
│   ├── work_time.py            # Cấu hình giờ làm
│   ├── help_command.py         # Help menu
│   ├── spam_control.py         # Anti-spam
│   ├── dm_control.py           # DM handler
│   └── offline_monitor.py      # Theo dõi offline
├── services/                    # Business logic
│   ├── violation_logger.py     # Ghi log vi phạm
│   ├── auto_warning_service.py # Cảnh báo tự động
│   ├── work_time_service.py    # Work time logic
│   └── excel_export_service.py # Xuất Excel
├── utils/                       # Utilities
│   ├── calendar_view.py        # Calendar UI
│   ├── time_picker_view.py     # Time picker UI
│   └── datetime_utils.py       # Date/time helpers
└── backups/                     # Backup files
```

## 🗄️ Database Schema

### Tables

**1. attendances** - Chấm công
- id, user_id, username, date
- checkin_time, checkout_time
- total_seconds

**2. breaks** - Nghỉ giải lao
- id, attendance_id, user_id
- start_time, end_time
- duration_seconds, note

**3. work_times** - Cấu hình giờ làm
- id, user_id, username
- start_time, end_time
- break_min_minutes, break_max_minutes
- is_group_default

**4. forgot_attendances** - Quên chấm công
- id, user_id, username, date
- type (checkin/checkout/both)
- reason, added_by

**5. day_offs** - Ngày nghỉ
- id, user_id, username, date
- is_server_wide, reason
- added_by, added_time

**6. spam_control** - Anti-spam
- id, user_id, message_count
- last_message_time, warning_count
- muted_until

**7. server_config** - Cấu hình server
- id, setting_name, setting_value
- updated_by, updated_at

**8. offline_reports** - Báo cáo offline
- id, attendance_id, user_id
- start_time, end_time
- duration_seconds, reported

## ⚙️ Cấu Hình Nâng Cao

### Auto Warning Service

Hệ thống tự động cảnh báo vi phạm:

**Grace Periods (có thể cấu hình):**
- Check-in: 15 phút (mặc định)
- Check-out: 60 phút (mặc định)

**Cấu hình:**
```
/admin warning checkin_grace:20 checkout_grace:45
```

**Tính năng:**
- ⏰ Kiểm tra mỗi 5 phút
- 📨 Gửi DM tự động
- 📋 Log vào kênh vi phạm
- 🔄 Reset cảnh báo mỗi ngày

### Violation Types

1. **LATE_CHECKIN** - Đi muộn (> grace period)
2. **LATE_CHECKOUT** - Về muộn (> grace period)
3. **INSUFFICIENT_HOURS** - Làm thiếu giờ (< 8 giờ)
4. **FORGOT_CHECKIN** - Quên check-in
5. **FORGOT_CHECKOUT** - Quên check-out

### Discord Channels

Bot cần các kênh sau:

- `#chấm-công` - Chấm công chính
- `#thông-báo` - Thông báo chung
- `#log-vi-phạm` - Log vi phạm

**Tạo tự động:** Bot sẽ tìm hoặc tạo các kênh này khi cần.

## 🔒 Phân Quyền

### Owner (Chủ Server)
- ✅ Tất cả quyền
- ✅ Restore database
- ✅ Xóa dữ liệu

### Administrator
- ✅ Hầu hết lệnh admin
- ✅ Backup & Export
- ✅ Cấu hình hệ thống
- ✅ Quản lý chấm công
- ❌ Restore (chỉ owner)

### Member
- ✅ Check-in/out
- ✅ Break start/end
- ✅ Xem thông tin cá nhân
- ✅ Menu tương tác
- ❌ Lệnh admin

## 📊 Excel Export Chi Tiết

Xem hướng dẫn đầy đủ tại: [EXCEL_EXPORT_GUIDE.md](EXCEL_EXPORT_GUIDE.md)

**Tóm tắt:**
```
/admin export
```

**Kết quả:**
- 📁 File .xlsx với 6 sheets
- 🎨 Professional formatting
- 🟨 Highlight violations
- 📊 Summary statistics
- 💾 Lưu tại `backups/`

## 🚀 Production Deployment

### 1. VPS/Server

**Ubuntu/Debian:**
```bash
# Install Python
sudo apt update
sudo apt install python3.11 python3.11-venv

# Clone & setup
git clone <repo>
cd "code diem danh discord"
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run with systemd
sudo nano /etc/systemd/system/discord-bot.service
```

**Systemd service file:**
```ini
[Unit]
Description=Discord HR Bot
After=network.target

[Service]
Type=simple
User=your_user
WorkingDirectory=/path/to/bot
ExecStart=/path/to/bot/.venv/bin/python main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

**Enable & start:**
```bash
sudo systemctl enable discord-bot
sudo systemctl start discord-bot
sudo systemctl status discord-bot
```

### 2. Docker (Recommended)

**Dockerfile:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
```

**docker-compose.yml:**
```yaml
version: '3.8'
services:
  bot:
    build: .
    environment:
      - DISCORD_TOKEN=${DISCORD_TOKEN}
    volumes:
      - ./attendance.db:/app/attendance.db
      - ./backups:/app/backups
    restart: unless-stopped
```

**Run:**
```bash
docker-compose up -d
```

### 3. Heroku

```bash
heroku create discord-hr-bot
heroku config:set DISCORD_TOKEN=your_token
git push heroku main
```

## 🔧 Troubleshooting

### Bot không online?

**Kiểm tra:**
1. Token đúng trong `.env`?
2. Bot được invite với đủ quyền?
3. Python version >= 3.11?

**Quyền cần thiết:**
- Send Messages
- Embed Links
- Attach Files
- Read Message History
- Add Reactions
- Manage Channels (để tạo kênh)

### Lỗi database?

**Reset database:**
```bash
python init_db.py
```

**Backup trước khi reset:**
```
/admin backup
```

### Lệnh không hiện?

**Sync commands thủ công:**
```python
# Trong main.py, thêm:
await bot.tree.sync()
```

**Hoặc:**
- Kick bot ra khỏi server
- Invite lại với link mới
- Đợi 1-2 phút

### Lỗi openpyxl?

```bash
pip install openpyxl
```

### File Excel quá lớn?

Discord giới hạn 8MB. Giải pháp:
1. Export theo tháng
2. Nén file (zip)
3. Upload lên cloud

## 📈 Performance Tips

### Database Optimization

**Index thường dùng:**
```sql
CREATE INDEX idx_attendance_date ON attendances(date);
CREATE INDEX idx_attendance_user ON attendances(user_id);
CREATE INDEX idx_breaks_date ON breaks(date);
```

**Cleanup old data:**
```python
# Delete data older than 1 year
session.query(Attendance).filter(
    Attendance.date < '2024-01-01'
).delete()
```

### Memory Usage

**Monitor:**
```bash
# Linux
ps aux | grep python

# Windows Task Manager
```

**Optimize:**
- Limit query results
- Close sessions properly
- Use background tasks wisely

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📝 TODO / Roadmap

- [ ] Web dashboard
- [ ] REST API
- [ ] Biometric integration
- [ ] Multiple servers support
- [ ] Role-based work times
- [ ] Overtime tracking
- [ ] Leave request workflow
- [ ] Integration với Google Sheets
- [ ] Mobile app notifications
- [ ] AI-powered insights

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author

Developed with ❤️ for HR management automation.

## 🙏 Acknowledgments

- Discord.py community
- SQLAlchemy documentation
- OpenPyXL contributors

## 📞 Support

**Có vấn đề?**
1. Kiểm tra [Troubleshooting](#-troubleshooting)
2. Xem [EXCEL_EXPORT_GUIDE.md](EXCEL_EXPORT_GUIDE.md)
3. Tạo issue trên GitHub

## 🔄 Changelog

### Version 4.0 (Latest)
- ✨ Excel export với 6 sheets
- ✨ Auto warning system
- ✨ Violation detection & logging
- ✨ Calendar UI cho date selection
- 🐛 Fixed forgot attendance tracking
- 🐛 Fixed permission issues

### Version 3.0
- ✨ Manual attendance commands
- ✨ Day off management
- ✨ Comprehensive reports
- 🎨 Improved UI with buttons

### Version 2.0
- ✨ Break management
- ✨ Work time configuration
- ✨ Spam control

### Version 1.0
- ✅ Basic check-in/out
- ✅ SQLite database
- ✅ Simple reports

---

**Made with ❤️ by Discord Bot Developers**

*Last updated: October 9, 2025*
