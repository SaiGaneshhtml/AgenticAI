to make the samller event to excuter with using multy thed anf  processing these work for 
hevey task not for task like (fetch api with 10 web app, sending req for app)here we use 
async 

in async there 4:
           1 is asynice func(also called as Coroutines )
           2 is await   this will wait untile the give time or task need done 
           3 is asyni.io  this is lib which help to perfoem all thes task and help us 
           4 event loop which will deiced which tack will excute 

to perform samller task we use asyc this our main gole to lern this 
here  expliantio  with a skill ton code

import async.io

anynce functio(name):
print ("{name }preparing chai..")
awaint.asynice.io(3)
print ("{name } chai done ..")


// this main fun we add 

async.main("masal1 chai","masal2 chai","masal3 chai")

asynceio.run(main())

// here i will get all masal 1,2,3 at a time 
this call non blaocking this spel for the asyci / await why we going use 
blocking 
we can use like sleep(2)
// oup will show m1 2sec  m2 sec m3  end 

this manjo diff 

async def
  → defines async function

await
  → wait without blocking other async tasks

asyncio
  → Python async framework

Event Loop
  → manages async tasks

asyncio.gather()
  → run independent async operations concurrently

asyncio.run()
  → starts the async program