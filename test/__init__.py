from test_event_api import TestRavenClient

test = TestRavenClient()
test.setUp()
test.test_send_bulk()
test.test_send()
