import React, {useEffect, useState} from 'react';
import { useSelector } from 'react-redux';
import axios from 'axios';
import './Home.css'

function Home( {setSelectedPost} ) {
  const [posts, setPosts] = useState([])
  const postsState = useSelector(state => state.allPosts.posts)

  useEffect(() => {
    axios.get('https://jsonplaceholder.typicode.com/photos').then(res => {
      // console.log(res.data)
      setPosts([...posts, ...res.data]) 
    })
  }, [])

  // useEffect(() => {
  //   console.log(posts)
  // }, [posts])

  return (
    <div className='posts'>
      { posts.map((post, index) => {
        return <div key={index} className='post' onClick={() => { setSelectedPost(post) }}>{post.title}</div>
      }) }
    </div>
  )
}

export default Home