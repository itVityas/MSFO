# # msfo1/middleware.py
#
# import logging
# from django.db import connection
#
# logger = logging.getLogger(__name__)
#
# class QueryLoggingMiddleware:
#     """
#     Middleware для логирования SQL-запросов, выполненных во время обработки запроса.
#     """
#
#     def __init__(self, get_response):
#         # Конструктор. Django вызывается один раз при запуске сервера.
#         self.get_response = get_response
#
#     def __call__(self, request):
#         """
#         Точка входа для каждого HTTP-запроса.
#         """
#         # --- Обработка "до" view (если нужно) ---
#         # Например, можно запоминать время начала и т.п.
#
#         response = self.get_response(request)
#
#         # --- Обработка "после" view ---
#         # В этот момент view уже отработал, и response готов.
#         # Здесь мы можем посмотреть, какие запросы к БД были выполнены.
#         # Коллекция django.db.connection.queries содержит все запросы
#         # (только при DEBUG=True)
#         queries = connection.queries
#
#         # Логируем общее количество запросов:
#         logger.info(f"Total DB queries: {len(queries)} for path: {request.path}")
#
#         # Если нужно вывести детальную информацию по запросам:
#         # (Учтите, что при большом количестве запросов это сильно засорит логи.)
#         for q in queries:
#             # q — словарь вида {"sql": "...", "time": "..." }
#             sql = q.get("sql", "")
#             time = q.get("time", "")
#             logger.debug(f"Query took {time} sec: {sql}")
#
#         return response
