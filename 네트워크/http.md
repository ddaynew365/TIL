# HTTP
- HTT는 state less이며 connection less이다.
- state less는 이전에 연결한 상태가 없다는 뜻이고 connection less는 비연결 지향형이라는 뜻이다.
- 따라서 TCP 위에서 동작하고 있는 HTTP는 매번 3-way, 4-way를 하여 연결을 하고 끊어야 했다.

## keep-Alive
- 원래는 데이터를 주고 받을 때마다 연결이 열고 닫히기를 반복해야하지만 keep alive를 설정하면 지정한 시간동안 데이터를 계속 주고 받아야한다. 
  => 즉, 데이터를 빈번하게 주고 받아야 한다면 좋은 선택이 될 수 있다.
- 그러나 사실 keep-Alive는 성능 하락의 주범인 경우가 많다.
  => 사용자가 많다면 연결이 늘어나서 새로운 사용자를 받아들이지 못하는 경우가 빈번히 일어난다. 그래서 사용자가 많고 유동이 많은 서비스에서는 사용이 권장하지 않는다.
