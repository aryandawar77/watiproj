'use client';

import Image from 'next/image'
import { Inter } from '@next/font/google'
import styles from './page.module.css'
import { useState } from 'react'
import axios from 'axios';

const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  const [number1, setNum1] = useState<any>();
  const [number2, setNum2] = useState<any>();
  const [sum, setSum] = useState<any>();
  const doSum = async()=>{
    const response = await axios.post('http://127.0.0.1:8000/api/add/',{
      "num1":number1,
      "num2":number2
  });

  console.log(response.data)
  setSum(response.data.sum)
  setNum1(undefined)
  setNum2(undefined)
  }

  const submit=()=>{
    doSum()
  }
  return (
    <div>
      <input placeholder='Number 1' type={'number'} onChange={(e)=>(setNum1(e.target.value))} value={number1}></input>
      <input placeholder='Number 2' type={'number'} onChange={(e)=>(setNum2(e.target.value))} value={number2}></input>
      <button onClick={()=>submit()}>Submit</button>
      <h1>SUM:{sum}</h1>{}
      {/* {number1},   {number2} */}
    </div>
  )
}
