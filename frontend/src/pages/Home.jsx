import React, {useEffect, useState} from 'react';
import axios from 'axios';
import './Home.css'

function Home() {
  const [posts, setPosts] = useState([])

  useEffect(() => {
    axios.get('https://jsonplaceholder.typicode.com/posts').then(res => {
      // console.log(res.data)
      setPosts([...posts, ...res.data]) 
    })
  }, [])

  useEffect(() => {
    console.log(posts)
  }, [posts])

  return (
    <div className='posts'>
      { posts.map((post, index) => {
        return <div className='post'>{post.title}</div>
      }) }
    </div>
  )
}

export default Home