# Asyncio exam
asyncio 库使用的例子
参考： http://asyncio.readthedocs.io


## 例子目录
* hello, hello_clock: 最基础的使用 asyncio event loop 运行 coroutine 任务的例子
* echo_tcp: asyncio 是 start_server 和 open_connection 的使用示例
* producer_consumer: 是使用 asyncio queue 作为协程间数据传递的方式，协作用例
* subthread_subprocess: 在协程中使用线程池和子进程来运行任务的使用示例
* web_craper: 使用 asyncio tcp 构建异步http爬虫的示例
* asyncio_http_example: 使用 aiohttp 库作为 http 客户端

## 小结
* python 协程 coroutine 是基于 yield 的特性
* python3.5+ 新增关键字 async, await 用于快速声明协程和执行协程
* 协程需要依赖 event_loop 运行，由event_loop 进行调度
* 线程的上下文切换是由 OS 调度，需要切出点不可预测，需要考虑资源竞争；协程切换需要自身主动让出执行权
（当使用 await 执行阻塞任务时），协程event_loop 时在一个线程内
* python GIL （https://wiki.python.org/moin/GlobalInterpreterLock）的存在，造成同一解析器运行进程内，
同一时刻只能有一个线程执行 python 字节码的解析，这使得python没法利用CPU多核特性，和单核一样；线程上下文切换
的代价远远比协程切换大，所以协程效率更高；多进程不受GIL影响，但是多进程占用的系统资源更大，且需要考虑进程间
数据共享问题。
* 协程虽然有诸多好处，但是协程这种异步模型有个特点，就是不能存在阻塞线程的代码，比如 socket.read() 会阻塞掉
整个线程， 所以其他的协程也不能运行了，这种"传染性"会导致整个项目都需要协程异步化，很多第现有库也需要用“异步化”
版本代替。
