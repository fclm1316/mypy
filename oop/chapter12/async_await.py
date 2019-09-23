#!/usr/bin/python3
#coding:utf-8
#使用关键字定义协程
async def downloader(url):
    return 'hah'

async def download_url(url):
    # yield from 交出控制权,等待downloader
    html = await downloader(url)
    return html


if __name__ == "__main__":
    coro = download_url('http://1111.com')
    coro.send(None)
