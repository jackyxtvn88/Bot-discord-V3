from typing import Optional, Any
from sqlalchemy import String, Integer, DateTime, Text, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Session, Mapped, mapped_column
from datetime import datetime

Base = declarative_base()

class SpamControl(Base):
    __tablename__ = 'spam_control'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[str] = mapped_column(String(20), nullable=False)
    message_count: Mapped[int] = mapped_column(Integer, default=0)
    last_message_time: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)
    warning_count: Mapped[int] = mapped_column(Integer, default=0)
    muted_until: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)

    def __init__(self, **kw: Any):
        for key, value in kw.items():
            setattr(self, key, value)

class ServerConfig(Base):
    __tablename__ = 'server_config'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    setting_name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    setting_value: Mapped[str] = mapped_column(Text, nullable=False)
    updated_by: Mapped[str] = mapped_column(String(20), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, **kw: Any):
        for key, value in kw.items():
            setattr(self, key, value)

class WorkTime(Base):
    __tablename__ = 'work_times'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[str] = mapped_column(String(20), nullable=False)
    username: Mapped[str] = mapped_column(String(100), nullable=False)
    start_time: Mapped[str] = mapped_column(String(5), nullable=False)  # Format: "HH:MM"
    end_time: Mapped[str] = mapped_column(String(5), nullable=False)    # Format: "HH:MM"
    break_min_minutes: Mapped[int] = mapped_column(Integer, default=30)  # Minimum break time
    break_max_minutes: Mapped[int] = mapped_column(Integer, default=60)  # Maximum break time
    is_group_default: Mapped[bool] = mapped_column(Boolean, default=False)  # If this is a group default setting

    def get_start_time(self):
        """Chuyển đổi start_time string thành time object"""
        hour, minute = map(int, self.start_time.split(':'))
        return datetime.now().replace(hour=hour, minute=minute, second=0, microsecond=0).time()
    
    def get_end_time(self):
        """Chuyển đổi end_time string thành time object"""
        hour, minute = map(int, self.end_time.split(':'))
        return datetime.now().replace(hour=hour, minute=minute, second=0, microsecond=0).time()

class Attendance(Base):
    __tablename__ = 'attendances'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[str] = mapped_column(String(20), nullable=False)
    username: Mapped[str] = mapped_column(String(100), nullable=False)
    date: Mapped[str] = mapped_column(String(10), nullable=False)
    checkin_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    checkout_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    total_seconds: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    breaks: Mapped[list["Break"]] = relationship("Break", back_populates="attendance")
    offline_reports: Mapped[list["OfflineReport"]] = relationship("OfflineReport", back_populates="attendance")

    def __init__(self, **kw: Any):
        for key, value in kw.items():
            setattr(self, key, value)

class Break(Base):
    __tablename__ = 'breaks'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    attendance_id: Mapped[int] = mapped_column(Integer, ForeignKey('attendances.id'))
    user_id: Mapped[str] = mapped_column(String(20), nullable=False)
    date: Mapped[str] = mapped_column(String(10), nullable=False)
    start_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    duration_seconds: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    note: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    warned: Mapped[bool] = mapped_column(Boolean, default=False)  # If a warning was sent for this break
    attendance: Mapped["Attendance"] = relationship("Attendance", back_populates="breaks")

    def __init__(self, **kw: Any):
        for key, value in kw.items():
            setattr(self, key, value)

class OfflineReport(Base):
    __tablename__ = 'offline_reports'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    attendance_id: Mapped[int] = mapped_column(Integer, ForeignKey('attendances.id'))
    user_id: Mapped[str] = mapped_column(String(20), nullable=False)
    start_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_time: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    duration_seconds: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    reported: Mapped[bool] = mapped_column(Boolean, default=False)  # If this offline period was reported
    attendance: Mapped["Attendance"] = relationship("Attendance", back_populates="offline_reports")

    def __init__(self, **kw: Any):
        for key, value in kw.items():
            setattr(self, key, value)

class ForgotAttendance(Base):
    __tablename__ = 'forgot_attendances'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[str] = mapped_column(String(20), nullable=False)
    username: Mapped[str] = mapped_column(String(100), nullable=False)
    date: Mapped[str] = mapped_column(String(10), nullable=False)
    type: Mapped[str] = mapped_column(String(20), nullable=False)  # 'checkin', 'checkout', 'breakout'
    added_by: Mapped[str] = mapped_column(String(20), nullable=False)
    added_by_name: Mapped[str] = mapped_column(String(100), nullable=False)
    added_time: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)
    reason: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)

    def __init__(self, **kw: Any):
        for key, value in kw.items():
            setattr(self, key, value)

class DayOff(Base):
    __tablename__ = 'day_offs'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[str] = mapped_column(String(20), nullable=False)
    username: Mapped[str] = mapped_column(String(100), nullable=False)
    date: Mapped[str] = mapped_column(String(10), nullable=False)
    is_server_wide: Mapped[bool] = mapped_column(Boolean, default=False)  # If this is a server-wide day off
    reason: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    added_by: Mapped[str] = mapped_column(String(20), nullable=False)
    added_by_name: Mapped[str] = mapped_column(String(100), nullable=False)
    added_time: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, **kw: Any):
        for key, value in kw.items():
            setattr(self, key, value)