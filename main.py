from control import click_next_friend_type, open_douyin_background, click_next_friend
import asyncio

async def main():
    await open_douyin_background()
    a = True
    while a:
        await click_next_friend_type()
        while a:
            import ipdb;ipdb.set_trace()
            await click_next_friend()
    

if __name__ == "__main__":
    asyncio.run(main())
    print('done')

