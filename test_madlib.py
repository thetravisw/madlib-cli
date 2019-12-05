from madlib import read_file, parse_string_and_inputs
from io import StringIO

def test_file_reader():
  expected = "In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to eat: it was a hobbit-hole, and that means comfort."
  actual = read_file("4tests.txt")
  assert actual == expected

def test_parse_string_and_inputs(monkeypatch):
  expected = "here be Genuine User Input!!"
  monkeypatch.setattr('sys.stdin', StringIO("Genuine User Input\n"))
  actual = parse_string_and_inputs("here be {input}!!")
  assert actual == expected        
