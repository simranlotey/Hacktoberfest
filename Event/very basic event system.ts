type HandlerOfevent = (...args: any[]) => void;

class EventEmitter {
  event: { [NameOfEvent: string]: HandlerOfevent[] };

  constructor() 
  {
    this.event = {};
  }

  on(NameOfEvent: string, handler: HandlerOfevent) 
  {
    if (!this.event[NameOfEvent]) {
      this.event[NameOfEvent] = [];
    }
    this.event[NameOfEvent].push(handler);
  }

  emit(NameOfEvent: string, ...args: any[])
   {
    const HandlerOfevents = this.event[NameOfEvent];
    if (HandlerOfevents) 
    {
      for (const handler of HandlerOfevents) 
      {
        handler(...args);
      }
    }
  }
}
//TestCases
const eventMaker = new EventEmitter();

const listener = (data: string) => {
  console.log(`data received: ${data}`);
};
eventMaker.on("event1", listener);

eventMaker.emit("event1", "this is a test lmao");
