# Что такое класс, атрибуты, методы и объект?
#
# class TestStep:
#     def __init__(self, name: str, status: str = "PASS", details: str | None = None):
#         self.name = name
#         self.status = status
#         self.details = details
#
#     @staticmethod
#     def check_status(status):
#         if status not in ('PASS', 'FAIL'):
#             raise ValueError('Invalid status')
#         return status
#
#     @property
#     def status(self):
#         return self._status
#
#     @status.setter
#     def status(self, status):
#         self._status = self.check_status(status)
#
#
#     def to_dict(self):
#         return {
#             'name': self.name,
#             'status': self.status,
#             'details': self.details
#         }
#
#     def format_line(self):
#         if self.details is None:
#             return f'[{self.status}] {self.name}'
#         return f'[{self.status}] {self.name} - {self.details}'
#
#
# step1 = TestStep("Open login page")
# step2 = TestStep("Enter credentials", details="user=admin")
# step3 = TestStep("Click login", status="FAIL", details="button disabled")
# print(step2.to_dict())
# print(step1.format_line())
# print(step3.format_line())
#
# class TestCase:
#     def __init__(self, title: str):
#         self.title = title
#         self.steps = []
#
#     def add_step(self, step: TestStep) -> None:
#         if not isinstance(step, TestStep):
#             raise TypeError
#         self.steps.append(step)
#
#     def is_passed(self) -> bool:
#         if not self.steps:
#             return False
#         for s in self.steps:
#             if s.status != 'PASS':
#                 return False
#         return True
#
#     def summary(self) -> str:
#         status = self.is_passed()
#         return f'{self.title}: {"PASS" if status else "FAIL"} ({len(self.steps)} steps)'
#
#
# case = TestCase("Login test")
# case.add_step(step1)
# case.add_step(step2)
# case.add_step(step3)
#
# print(case.is_passed())
# print(case.summary())
import functools
from itertools import count
from xml.dom import ValidationErr

#######################################################################################################################
# Наследование

# class BasePage:
#     def __init__(self, url: str):
#         self.url = url
#
#     def open(self):
#         return f'OPEN {self.url}'
#
#     def render(self) -> str:
#         return "Render: base"
#
#
# class LoginPage(BasePage):
#     def __init__(self, url: str, username_field: str, password_field: str):
#         super().__init__(url)
#         self.username_field = username_field
#         self.password_field = password_field
#
#     def open(self):
#         return f'OPEN {self.url} (login)'
#
#     def render(self) -> str:
#         return "Render: login form"
#
#
# class DashboardPage(BasePage):
#     def __init__(self, url: str, user: str):
#         super().__init__(url)
#         self.user = user
#
#     def greeting(self) -> str:
#         return f'Hello, {self.user}!'
#
#     def render(self) -> str:
#         return f'Render: dashboard for {self.user}'
#
#
# login = LoginPage("https://site.test/login", "#user", "#pass")
# dash = DashboardPage("https://site.test/dashboard", "admin")
#
# print(login.open())
# print(dash.open())
# print(dash.greeting())
#
# def render_all(pages: list[BasePage]) -> list[str]:
#     res = [p.render() for p in pages]
#     return res
#
# pages = [
#     LoginPage("https://site.test/login", "#user", "#pass"),
#     DashboardPage("https://site.test/dashboard", "admin"),
# ]
# print(render_all(pages))

#######################################################################################################################
# Инкапсуляция

# class BankAccount:
#     def __init__(self, owner: str, balance: int = 0):
#         if balance < 0:
#             raise ValueError
#         self.__balance = balance
#         self.owner = owner
#
#     @staticmethod
#     def check_value(value):
#         if value <= 0:
#             raise ValueError
#         return value
#
#     @property
#     def balance(self):
#         return self.__balance
#
#     def deposit(self, amount: int) -> None:
#         self.check_value(amount)
#         self.__balance += amount
#
#     def withdraw(self, amount: int) -> None:
#         self.check_value(amount)
#         if self.__balance < amount:
#             raise ValueError
#         self.__balance -= amount
#
#
# acc = BankAccount("Misha", 100)
# acc.deposit(50)
# acc.withdraw(120)
# print(acc.balance)   # ожидаем 30

# class UserProfile:
#     def __init__(self, username: str, email: str):
#         self.username = username
#         self.__email = email
#
#     @property
#     def email(self):
#         return self.__email
#
#     def set_email(self, new_email: str) -> None:
#         if '@' not in new_email or new_email.count('@') > 1:
#             raise ValueError
#         elif '.' not in new_email.split('@')[1]:
#             raise ValueError
#         self.__email = new_email
#
#
# u = UserProfile("misha", "misha@test.com")
# print(u.email)              # misha@test.com
# u.set_email("new@site.org")
# print(u.email)              # new@site.org
#
# # u.set_email("nosymbol.com")
# # u.set_email("a@b.c@d.com")
# # u.set_email("bad@sitecom")

#######################################################################################################################
# Полиморфизм

# class Notifier:
#     def send(self, message: str) -> str:
#         raise NotImplementedError
#
#
# class EmailNotifier(Notifier):
#     def send(self, message: str):
#         return f'EMAIL: {message}'
#
#
# class SmsNotifier(Notifier):
#     def send(self, message: str):
#         return f'SMS: {message}'
#
#
# def notify_all(notifiers: list[Notifier], message: str) -> list[str]:
#     return [n.send(message) for n in notifiers]
#
# notifiers = [EmailNotifier(), SmsNotifier(), EmailNotifier()]
# print(notify_all(notifiers, "Build finished"))
#
# def safe_send(sender, message: str) -> str:
#     if not hasattr(sender, 'send'):
#         return 'ERROR: no send method'
#     try:
#         return sender.send(message)
#     except Exception:
#         return "ERROR: send failed"
#
# class BrokenNotifier:
#     def send(self, message: str) -> str:
#         raise RuntimeError("boom")
#
# print(safe_send(EmailNotifier(), "Hi"))
# print(safe_send("notifier", "Hi"))
# print(safe_send(BrokenNotifier(), "Hi"))

#######################################################################################################################
# Полиморфизм

# class ApiResponse:
#     def __init__(self, url: str, status_code: int, json_body: dict):
#         self.url = url
#         self.status_code = status_code
#         if not isinstance(json_body, dict):
#             raise TypeError
#         self.json_body = json_body
#
#     def summary(self) -> str:
#         if 200 <= self.status_code <= 299:
#             return f'PASS {self.status_code} {self.url}'
#         return f'FAIL {self.status_code} {self.url}'
#
#     @staticmethod
#     def is_valid_status_code(code: int) -> bool:
#         if isinstance(code, int) and 100 <= code <= 599:
#             return True
#         return False
#
#     @classmethod
#     def from_raw(cls, raw: dict) -> "ApiResponse":
#         if not cls.is_valid_status_code(raw['status_code']):
#             raise ValueError
#         return cls(raw['url'], raw['status_code'], raw['json'])
#
#
# raw_ok = {
#     "url": "https://api.test/users/1",
#     "status_code": 200,
#     "json": {"id": 1, "name": "Misha"}
# }
#
# raw_bad = {
#     "url": "https://api.test/users/999",
#     "status_code": 404,
#     "json": {"error": "Not Found"}
# }
#
# raw_invalid = {
#     "url": "https://api.test/users",
#     "status_code": 700,
#     "json": {}
# }
#
# r1 = ApiResponse.from_raw(raw_ok)
# r2 = ApiResponse.from_raw(raw_bad)
#
# print(r1.summary())  # PASS 200 https://api.test/users/1
# print(r2.summary())  # FAIL 404 https://api.test/users/999
#
# # ApiResponse.from_raw(raw_invalid)  # ValueError
# print(ApiResponse.is_valid_status_code("200"))  # False

# class User:
#     def __init__(self, username: str, is_active: bool):
#         self.username = username
#         self.is_active = is_active
#
#     def label(self) -> str:
#         if self.is_active:
#             status = 'active'
#         else:
#             status = 'inactive'
#         return f'{self.username}: {status}'
#
#     @staticmethod
#     def is_valid_username(name: str) -> bool:
#         if not isinstance(name, str):
#             return False
#         elif not 3 <= len(name) <= 12:
#             return False
#         elif not name.replace('_', '').isalnum():
#             return False
#         return True
#
#     @classmethod
#     def from_dict(cls, data: dict):
#         if not cls.is_valid_username(data['username']):
#             raise ValueError
#         return cls(data['username'], data['active'])
#
#
# class AdminUser(User):
#     def __init__(self, username: str, is_active: bool, role: str = 'admin'):
#         super().__init__(username, is_active)
#         self.role = role
#
#     def label(self) -> str:
#         if self.is_active:
#             status = 'active'
#         else:
#             status = 'inactive'
#         return f'{self.username} ({self.role}): {status}'
#
#
# u = User.from_dict({"username": "misha_1", "active": True})
# a = AdminUser.from_dict({"username": "root", "active": False})
#
# print(type(u).__name__)   # User
# print(type(a).__name__)   # AdminUser
#
# print(u.label())          # misha_1: active
# print(a.label())          # root (admin): inactive
#
# # User.from_dict({"username": "mi", "active": True})      # ValueError
# # User.from_dict({"username": "bad name", "active": True})# ValueError

# from functools import total_ordering
# @total_ordering
# class TestRun:
#     def __init__(self, run_id: str, steps: list[str], duration_sec: int):
#         self.run_id = run_id
#         self.steps = steps
#         self.duration_sec = duration_sec
#
#     def __len__(self):
#         return len(self.steps)
#
#     def __bool__(self):
#         if not len(self.steps):
#             return False
#         else:
#             return True
#
#     def __str__(self):
#         return f'Run {self.run_id}: {len(self.steps)} steps, {self.duration_sec}s'
#
#     def __repr__(self):
#         return f"{self.__class__.__name__}(run_id='{self.run_id}', steps={len(self.steps)}, duration_sec={self.duration_sec})"
#
#     def __eq__(self, other):
#         if not isinstance(other, TestRun):
#             return NotImplemented
#         return self.run_id == other.run_id
#
#     def __lt__(self, other):
#         if not isinstance(other, TestRun):
#             return NotImplemented
#         return self.duration_sec < other.duration_sec
#
#
# r1 = TestRun("R1", ["open", "login", "logout"], 12)
# r2 = TestRun("R2", ["open"], 5)
# r3 = TestRun("R1", ["anything"], 99)
# r0 = TestRun("R0", [], 1)
#
# print(len(r1))         # 3
# print(bool(r0))        # False
# print(str(r2))         # Run R2: 1 steps, 5s
# print([r2])            # [TestRun(run_id='R2', steps=1, duration_sec=5)]
#
# print(r1 == r3)        # True
# print(r1 == r2)        # False
#
# print(r2 < r1)         # True (5 < 12)
#
# print(sorted([r1, r2], key=lambda x: x))  # должно работать через __lt__
# # ожидаемый порядок: сначала r2, потом r1

# class EnvFlag:
#     def __init__(self, env: dict, key: str, value: str):
#         self.env = env
#         self.key = key
#         self.value = value
#
#     def __enter__(self):
#         self.old_env = self.env.get(self.key)
#         self.env[self.key] = self.value
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.old_env is None:
#             del self.env[self.key]
#         else:
#             self.env[self.key] = self.old_env
#         return False
#
# env = {"MODE": "prod"}
#
# try:
#     with EnvFlag(env, "MODE", "test"):
#         print(env["MODE"])     # test
#         raise RuntimeError("boom")
# except RuntimeError:
#     pass
#
# print(env["MODE"])             # prod
#
# with EnvFlag(env, "NEW_FLAG", "1"):
#     print(env["NEW_FLAG"])     # 1
#
# print("NEW_FLAG" in env)       # False

# from contextlib import contextmanager
#
# @contextmanager
# def env_flag(env: dict, key: str, value: str):
#     try:
#         old_value = env.get(key)
#         was_key = key in env
#         env[key] = value
#         yield env
#     finally:
#         if not was_key:
#             del env[key]
#         else:
#             env[key] = old_value
#
# env = {"MODE": "prod"}
#
# try:
#     with env_flag(env, "MODE", "test"):
#         print(env["MODE"])     # test
#         raise RuntimeError("boom")
# except RuntimeError:
#     pass
#
# print(env["MODE"])             # prod
#
# with env_flag(env, "NEW_FLAG", "1"):
#     print(env["NEW_FLAG"])     # 1
#
# print("NEW_FLAG" in env)       # False

#######################################################################################################################
# Декораторы

# from functools import wraps
# def log_calls(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f'CALL {func.__name__}')
#         return func(*args, **kwargs)
#     return wrapper
#
# @log_calls
# def add(a, b):
#     """Adds two numbers."""
#     return a + b
#
# @log_calls
# def greet(name="Misha"):
#     return f"Hi, {name}"
#
# print(add(2, 3))
# print(greet())
# print(add.__name__)   # add
# print(add.__doc__)    # Adds two numbers.

# from functools import wraps
#
# def retry(times: int):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             last_exc = None
#
#             for _ in range(times):
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as e:
#                     last_exc = e
#
#             raise last_exc
#         return wrapper
#     return decorator
#
# calls = {"n": 0}
#
# @retry(times=3)
# def sometimes_fails():
#     calls["n"] += 1
#     if calls["n"] < 3:
#         raise ValueError("fail")
#     return "ok"
#
# print(sometimes_fails())   # ok
# print(calls["n"])          # 3
#
# calls2 = {"n": 0}
#
# @retry(times=2)
# def always_fails():
#     calls2["n"] += 1
#     raise RuntimeError("boom")
#
# try:
#     always_fails()
# except RuntimeError:
#     print("caught")
# print(calls2["n"])         # 2

#######################################################################################################################
# Генераторы

# def iter_errors(lines: list[str]):
#     for l in lines:
#         status = l.split(':')[0].strip()
#         if status == 'ERROR':
#             yield l
#
# lines = [
#     "INFO: started",
#     "ERROR: timeout",
#     "WARN: retry",
#     "ERROR: bad response",
#     "INFO: done",
# ]
#
# gen = iter_errors(lines)
#
# print(next(gen))   # ERROR: timeout
# print(list(gen))   # ["ERROR: bad response"]

# def batched(items, batch_size):
#     if batch_size <= 0:
#         raise ValueError
#     num_of_lists = len(items) // batch_size + (0 if len(items) % batch_size == 0 else 1)
#     i = 0
#     for n in range(i, len(items), batch_size):
#         yield items[i:i + batch_size]
#         i += batch_size
#
# data = [1, 2, 3, 4, 5, 6, 7]
#
# print(list(batched(data, 3)))
# # ожидаем: [[1, 2, 3], [4, 5, 6], [7]]
#
# print(list(batched([], 3)))
# # ожидаем: []
# print(list(batched([1,2,3,4,5,6,7,8,9,10], 3)))

#######################################################################################################################
# ООП

# class Artifact:
#     def __init__(self, name: str):
#         self.name = name
#
#     def render(self) -> str:
#         raise NotImplementedError
#
#
# class Screenshot(Artifact):
#     def __init__(self, name: str, path: str):
#         super().__init__(name)
#         self.path = path
#
#     def render(self) -> str:
#         return f'IMG {self.name}: {self.path}'
#
#
# class TextLog(Artifact):
#     def __init__(self, name: str, lines: list[str]):
#         super().__init__(name)
#         self.lines = lines
#
#     def render(self) -> str:
#         return f'LOG {self.name}: {len(self.lines)} lines'
#
#
# class JsonDump(Artifact):
#     def __init__(self, name: str, data: dict):
#         super().__init__(name)
#         self.data = data
#
#     def render(self) -> str:
#         return f'JSON {self.name}: {len(self.data)} keys'
#
#
# class TestReport:
#     def __init__(self, title: str):
#         self.title = title
#         self.__artifacts = []
#
#     def add(self, artifact: Artifact) -> None:
#         if not isinstance(artifact, Artifact):
#             raise TypeError
#         self.__artifacts.append(artifact)
#
#     def render_all(self) -> list[str]:
#         return [s.render() for s in self.__artifacts]
#
#     @property
#     def artifacts_count(self):
#         return len(self.__artifacts)
#
# report = TestReport("Login test")
#
# report.add(Screenshot("after_login", "/tmp/1.png"))
# report.add(TextLog("browser", ["GET /login", "POST /login", "200 OK"]))
# report.add(JsonDump("response", {"id": 1, "name": "Misha"}))
#
# print(report.artifacts_count)       # 3
# print(report.render_all())
# # [
# #   "IMG after_login: /tmp/1.png",
# #   "LOG browser: 3 lines",
# #   "JSON response: 2 keys"
# # ]
#
# # report.add("not artifact")          # TypeError

# class Connection:
#     def __init__(self, conn_id: int):
#         self.__conn_id = conn_id
#
#     def request(self, endpoint: str) -> str:
#         return f'conn {self.__conn_id} -> {endpoint}'
#
#
# class ConnectionPool:
#     def __init__(self, limit: int):
#         if limit <= 0:
#             raise ValueError
#         self.__limit = limit
#         self.__active = 0
#         self.__next_id = 1
#
#     def acquire(self) -> Connection:
#         if self.__active == self.__limit:
#             raise RuntimeError
#         else:
#             self.__active += 1
#         self.__next_id += 1
#         return Connection(self.__next_id - 1)
#
#     def release(self) -> None:
#         if self.__active == 0:
#             raise RuntimeError
#         self.__active -= 1
#
#     @property
#     def active(self):
#         return self.__active
#
#
# pool = ConnectionPool(limit=2)
#
# c1 = pool.acquire()
# c2 = pool.acquire()
#
# print(pool.active)              # 2
# print(c1.request("/users"))     # conn 1 -> /users
# print(c2.request("/health"))    # conn 2 -> /health
#
# # pool.acquire()                  # RuntimeError (лимит)
#
# pool.release()
# print(pool.active)              # 1
#
# c3 = pool.acquire()
# print(c3.request("/ping"))      # conn 3 -> /ping
# print(pool.active)              # 2
#
# pool.release()
# pool.release()
# # pool.release()                  # RuntimeError (слишком много release)

#######################################################################################################################
# SOLID

#######################################################################################################################
# Дескрипторы

# class NonNegativeInt:
#     @staticmethod
#     def positive_int(val):
#         if not isinstance(val, int):
#             raise TypeError
#         elif val < 0:
#             raise ValueError
#
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         return instance.__dict__.get(self.name, 0)
#
#     def __set__(self, instance, value):
#         self.positive_int(value)
#         setattr(instance, self.name, value)
#
#
# class TestStep:
#     duration_ms = NonNegativeInt()
#     def __init__(self, name: str, duration_ms: int = 0):
#         self.name = name
#         self.duration_ms = duration_ms
#
#
# s = TestStep("login")
# print(s.duration_ms)              # 0
#
# s.duration_ms = 120
# print(s.duration_ms)              # 120
#
# try:
#     s.duration_ms = -1
# except ValueError:
#     print("ValueError")
#
# try:
#     s.duration_ms = "100"
# except TypeError:
#     print("TypeError")
#
# print(isinstance(TestStep.duration_ms, NonNegativeInt))  # True

# class EmailField:
#     @classmethod
#     def validator(cls, value):
#         if not isinstance(value, str):
#             raise TypeError
#         elif value.count('@') != 1 or '.' not in value.split('@')[1] or value.endswith('.'):
#             raise ValueError
#
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         return getattr(instance, self.name, None)
#
#     def __set__(self, instance, value):
#         self.validator(value)
#         setattr(instance, self.name, value)
#
#
# class User:
#     email = EmailField()
#     def __init__(self, email: str | None = None):
#         if email is not None:
#             self.email = email
#
#
# u = User()
# print(u.email)  # None
#
# u.email = "misha@test.com"
# print(u.email)  # misha@test.com
# print(u._email) # misha@test.com
#
# try:
#     u.email = "bad@sitecom"
# except ValueError:
#     print("ValueError")
#
# try:
#     u.email = "a@b.c@d.com"
# except ValueError:
#     print("ValueError2")
#
# try:
#     u.email = 123
# except TypeError:
#     print("TypeError")
#
# print(isinstance(User.email, EmailField))  # True

#######################################################################################################################
# Dataclasses

from dataclasses import dataclass, field
# @dataclass(order=True)
# class TestUser:
#     name: str
#     age: int
#
# u1 = TestUser("Anna", 25)
# u2 = TestUser("Anna", 25)
# u3 = TestUser("Misha", 30)
# u4 = TestUser("Boris", 25)
#
# print(u1)                 # TestUser(name='Anna', age=25)
# print(u1 == u2)           # True
# print(u1 == u3)           # False
#
# print(sorted([u3, u4, u1]))
# # ожидаем порядок:
# # [TestUser(name='Anna', age=25), TestUser(name='Boris', age=25), TestUser(name='Misha', age=30)]

@dataclass(frozen=True)
class StepResult:
    name: str
    status: str
    duration_ms: int

    def __post_init__(self):
        if self.status not in ('PASS', 'FAIL'):
            raise ValueError
        if self.duration_ms < 0:
            raise ValueError

    def short(self):
        return f'{self.status} {self.name} ({self.duration_ms}ms)'


s1 = StepResult("Open page", "PASS", 120)
# print(s1)                 # StepResult(name='Open page', status='PASS', duration_ms=120)
# print(s1.short())         # PASS Open page (120ms)
#
# try:
#     StepResult("X", "SKIP", 1)
# except ValueError:
#     print("ValueError1")
#
# try:
#     StepResult("X", "PASS", -5)
# except ValueError:
#     print("ValueError2")
#
# try:
#     s1.status = "FAIL"
# except Exception:
#     print("immutable")

# @dataclass
# class TestReport:
#     title: str
#     steps: list[StepResult] = field(default_factory=list)
#
#     def add(self, step: StepResult) -> None:
#         self.steps.append(step)
#
#     @property
#     def total_duration(self):
#         return sum([s.duration_ms for s in self.steps])
#
#     @property
#     def is_passed(self):
#         if not len(self.steps) > 0:
#             return False
#         elif 'FAIL' in [s.status for s in self.steps]:
#             return False
#         return True
#
#     def summary(self):
#         if 'FAIL' in [s.status for s in self.steps]:
#             return f'{self.title}: FAIL ({len(self.steps)} steps, {self.total_duration}ms)'
#         return f'{self.title}: PASS ({len(self.steps)} steps, {self.total_duration}ms)'
#
#
# r = TestReport("Login test")
#
# r.add(StepResult("Open page", "PASS", 120))
# r.add(StepResult("Enter creds", "PASS", 200))
# r.add(StepResult("Click login", "FAIL", 130))
#
# print(r.total_duration)   # 450
# print(r.is_passed)        # False
# print(r.summary())        # Login test: FAIL (3 steps, 450ms)
#
# r2 = TestReport("Empty")
# print(r2.is_passed)       # False

################################
# def generate_pairs(n):
#     res = []
#     for a in range(n + 1):
#         for b in range(a, n + 1):
#             res.append([a, b])
#     return res
# print(generate_pairs(2))


# def i_or_f(s: str) -> bool:
#     try:
#         int(s)
#         float(s)
#     except ValueError:
#         return False
#     else:
#         return True

# def reverse_words(text):
#     split_text = text.split(' ')
#     res_text = []
#     for el in split_text:
#         res_text.append(el[::-1])
#     return ' '.join(res_text)
# print(reverse_words('  double  spaced  words  '))
# print('  double  spaced  words  ')
