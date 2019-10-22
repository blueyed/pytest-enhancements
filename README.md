# pytest-enhancements

Enhancements to pytest that were rejected upstream.
Might involve monkey-patching pytest directly.. :/

See also [my pytest branch with more enhancements](https://github.com/blueyed/pytest/).

## Features

- Supports passing dictionaries to [@pytest.mark.parametrize](https://docs.pytest.org/en/latest/reference.html#pytest-mark-parametrize-ref):

  ```python
  @pytest.mark.parametrize('arg1,arg2,expected_id', {
      "myid_12": [1, 2, "[myid_12]"],
      "replaced_id": pytest.param(3, 4, "[replaced_id]", id="myid_34"),
      "myid_56": pytest.param(5, 6, "[myid_56]"),
  })
  def test_parametrize_dict(request, arg1, arg2, expected_id):
      if expected_id is None:
          expected_id = "[%d-%d-None]" % (arg1, arg2)
      assert request.node.nodeid.endswith(expected_id)
  ```
  (rejected in https://github.com/pytest-dev/pytest/pull/5850)

## Installation

    $ pip install pytest-enhancements

## License

Distributed under the terms of the
[GNU GPL v3.0](http://www.gnu.org/licenses/gpl-3.0.txt) license.
