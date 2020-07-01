<template>
  <div class="box">
    <el-row class="tac">
      <el-col :span="6">
        <el-menu
          default-active="2"
          class="el-menu-vertical-demo"
          @open="handleOpen"
          @close="handleClose">
          <el-submenu index="1">
            <template slot="title">
              <i class="el-icon-menu"></i>
              <span>佣金问题</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="1-1" @click="commissionTest1">基本边界值测试</el-menu-item>
              <el-menu-item index="1-2" @click="commissionTest2">健壮边界值测试</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-submenu index="2">
            <template slot="title">
              <i class="el-icon-menu"></i>
              <span>三角形类型</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="2-1" @click="triAngelTest1">基本边界值测试</el-menu-item>
              <el-menu-item index="2-2" @click="triAngelTest2">等价类测试</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-submenu index="3">
            <template slot="title">
              <i class="el-icon-menu"></i>
              <span>万年历问题</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="3-1" @click="calendarTest1">基本边界值测试</el-menu-item>
              <el-menu-item index="3-2" @click="calendarTest2">等价类测试</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-submenu index="4">
            <template slot="title">
              <i class="el-icon-menu"></i>
              <span>电信收费问题</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="4-1" @click="phoneTest1">健壮边界值测试</el-menu-item>
              <el-menu-item index="4-2" @click="phoneTest2">弱一般等价类测试</el-menu-item>
              <el-menu-item index="4-3" @click="phoneTest3">决策表测试</el-menu-item>
              <el-menu-item index="4-4" @click="phoneTest4">最优测试</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
        </el-menu>
      </el-col>
      <el-col :span="18">
        <el-table
          id="testtable"
          :data="tableData"
          stripe
          style="width: 100%">
          <el-table-column v-for="(item,index) in tableCol" :key="index"
          :prop="item.value"
          :label="item.name">
          </el-table-column>
        </el-table>
      </el-col>
    </el-row>
  </div>
</template>

<script>
/* eslint-disable */
export default {
    data() {
        return {
            tableData:[],
            tableCol:[]
        }
    },
    methods: {
        handleOpen(key, keyPath) {
            console.log(key, keyPath);
        },
        handleClose(key, keyPath) {
            console.log(key, keyPath);
        },
        commissionTest1(){
            this.tableCol=[
                {name:"主机", value:"mainframe"},
                {name:"显示器", value:"displayer"},
                {name:"外设", value:"peripheral"},
                {name:"预期结果", value:"presult"},
                {name:"测试结果", value:"rresult"},
                {name:"正误", value:"tf"},
            ];
            this.$axios.get('/getCommissionTest1')
                .then((response) => {
                    this.tableData=response.data;
                    for(let i=0;i<this.tableData.length;i++){
                        this.$axios.post('/commissionTest',
                            {
                                'mainframe':this.tableData[i].mainframe,
                                'displayer':this.tableData[i].displayer,
                                'peripheral':this.tableData[i].peripheral,
                                'index':i
                            })
                            .then((response) => {
                                let result=response.data;
                                this.changeData(result)
                            })
                    }
                });
            // this.tableData=[
            //     {mainframe:0,displayer:40,peripheral:45,presult:0},
            //     {mainframe:1,displayer:40,peripheral:45,presult:650},
            //     {mainframe:35,displayer:40,peripheral:45,presult:820},
            //     {mainframe:69,displayer:40,peripheral:45,presult:990},
            //     {mainframe:70,displayer:40,peripheral:45,presult:995},
            //     {mainframe:35,displayer:0,peripheral:45,presult:0},
            //     {mainframe:35,displayer:1,peripheral:45,presult:586},
            //     {mainframe:35,displayer:79,peripheral:45,presult:1054},
            //     {mainframe:35,displayer:80,peripheral:45,presult:1060},
            //     {mainframe:35,displayer:40,peripheral:0,presult:0},
            //     {mainframe:35,displayer:40,peripheral:1,presult:424},
            //     {mainframe:35,displayer:40,peripheral:89,presult:1216},
            //     {mainframe:35,displayer:40,peripheral:90,presult:1225}
            // ];
        },
        commissionTest2(){
            this.tableCol=[
                {name:"主机", value:"mainframe"},
                {name:"显示器", value:"displayer"},
                {name:"外设", value:"peripheral"},
                {name:"预期结果", value:"presult"},
                {name:"测试结果", value:"rresult"},
                {name:"正误", value:"tf"},
            ];
            // this.tableData=[
            //     {mainframe:-1,displayer:40,peripheral:45,presult:0},
            //     {mainframe:0,displayer:40,peripheral:45,presult:0},
            //     {mainframe:1,displayer:40,peripheral:45,presult:650},
            //     {mainframe:35,displayer:40,peripheral:45,presult:820},
            //     {mainframe:69,displayer:40,peripheral:45,presult:990},
            //     {mainframe:70,displayer:40,peripheral:45,presult:995},
            //     {mainframe:71,displayer:40,peripheral:45,presult:995},
            //     {mainframe:35,displayer:-1,peripheral:45,presult:0},
            //     {mainframe:35,displayer:0,peripheral:45,presult:0},
            //     {mainframe:35,displayer:1,peripheral:45,presult:586},
            //     {mainframe:35,displayer:79,peripheral:45,presult:1054},
            //     {mainframe:35,displayer:80,peripheral:45,presult:1060},
            //     {mainframe:35,displayer:81,peripheral:45,presult:1060},
            //     {mainframe:35,displayer:40,peripheral:-1,presult:0},
            //     {mainframe:35,displayer:40,peripheral:0,presult:0},
            //     {mainframe:35,displayer:40,peripheral:1,presult:424},
            //     {mainframe:35,displayer:40,peripheral:89,presult:1216},
            //     {mainframe:35,displayer:40,peripheral:90,presult:1225},
            //     {mainframe:35,displayer:40,peripheral:91,presult:1225}
            // ];
            this.$axios.get('/getCommissionTest2')
                .then((response) => {
                    this.tableData=response.data;
                    for(let i=0;i<this.tableData.length;i++){
                        this.$axios.post('/commissionTest',
                            {
                                'mainframe':this.tableData[i].mainframe,
                                'displayer':this.tableData[i].displayer,
                                'peripheral':this.tableData[i].peripheral,
                                'index':i
                            })
                            .then((response) => {
                                let result=response.data;
                                this.changeData(result)
                            })
                    }
                });
        },
        triAngelTest1(){
          this.tableCol=[
            {name:"x", value:"x"},
            {name:"y", value:"y"},
            {name:"z", value:"z"},
            {name:"预期结果", value:"presult"},
            {name:"测试结果", value:"rresult"},
            {name:"正误", value:"tf"},
          ];
          // this.tableData=[
          //   {x:100,y:100,z:1,presult:"等腰三角形"},
          //   {x:100,y:100,z:2,presult:"等腰三角形"},
          //   {x:100,y:100,z:100,presult:"等边三角形"},
          //   {x:100,y:100,z:199,presult:"等腰三角形"},
          //   {x:100,y:100,z:200,presult:"非三角形"},
          //   {x:100,y:1,z:100,presult:"等腰三角形"},
          //   {x:100,y:2,z:100,presult:"等腰三角形"},
          //   {x:100,y:199,z:100,presult:"等腰三角形"},
          //   {x:100,y:200,z:100,presult:"非三角形"},
          //   {x:1,y:100,z:100,presult:"等腰三角形"},
          //   {x:2,y:100,z:100,presult:"等腰三角形"},
          //   {x:199,y:100,z:100,presult:"等腰三角形"},
          //   {x:200,y:100,z:100,presult:"非三角形"}
          // ];
          this.$axios.get('/getTriAngelData1')
            .then((response) => {
              this.tableData=response.data;
              for(let i=0;i<this.tableData.length;i++){
                this.$axios.post('/triAngelTest',
                  {
                    'x':this.tableData[i].x,
                    'y':this.tableData[i].y,
                    'z':this.tableData[i].z,
                    'index':i
                  })
                  .then((response) => {
                    let result=response.data;
                    this.changeData(result)
                  })
              }
            });
        //   for(let i=0;i<this.tableData.length;i++){
        //     this.$axios.post('/triAngelTest',
        //       {
        //         'x':this.tableData[i].x,
        //         'y':this.tableData[i].y,
        //         'z':this.tableData[i].z,
        //         'index':i
        //       })
        //       .then((response) => {
        //         let result=response.data;
        //         this.changeData(result)
        //       })
        //   }
        },
        triAngelTest2(){
          this.tableCol=[
            {name:"x", value:"x"},
            {name:"y", value:"y"},
            {name:"z", value:"z"},
            {name:"预期结果", value:"presult"},
            {name:"测试结果", value:"rresult"},
            {name:"正误", value:"tf"},
          ];
          // this.tableData=[
          //   {x:3,y:4,z:5,presult:"一般三角形"},
          //   {x:3,y:3,z:4,presult:"等腰三角形"},
          //   {x:3,y:4,z:4,presult:"等腰三角形"},
          //   {x:3,y:4,z:3,presult:"等腰三角形"},
          //   {x:3,y:3,z:3,presult:"等边三角形"},
          //   {x:0,y:1,z:2,presult:"非三角形"},
          //   {x:1,y:0,z:2,presult:"非三角形"},
          //   {x:1,y:2,z:0,presult:"非三角形"},
          //   {x:1,y:2,z:3,presult:"非三角形"},
          //   {x:2,y:3,z:1,presult:"非三角形"},
          //   {x:3,y:2,z:1,presult:"非三角形"}
          // ];
          this.$axios.get('/getTriAngelData2')
            .then((response) => {
              this.tableData=response.data;
              for(let i=0;i<this.tableData.length;i++){
                this.$axios.post('/triAngelTest',
                  {
                    'x':this.tableData[i].x,
                    'y':this.tableData[i].y,
                    'z':this.tableData[i].z,
                    'index':i
                  })
                  .then((response) => {
                    let result=response.data;
                    this.changeData(result)
                  })
              }
            });
          // for(let i=0;i<this.tableData.length;i++){
          //   this.$axios.post('/triAngelTest',
          //     {
          //       'x':this.tableData[i].x,
          //       'y':this.tableData[i].y,
          //       'z':this.tableData[i].z,
          //       'index':i
          //     })
          //     .then((response) => {
          //       let result=response.data;
          //       this.changeData(result)
          //     })
          // }
        },
        calendarTest1(){
          this.tableCol=[
            {name:"year", value:"year"},
            {name:"month", value:"month"},
            {name:"date", value:"date"},
            {name:"预期结果", value:"presult"},
            {name:"测试结果", value:"rresult"},
            {name:"正误", value:"tf"},
          ];
          // this.tableData=[
          //   {year:2000,month:7,date:1,presult:6},
          //   {year:2000,month:7,date:2,presult:7},
          //   {year:2000,month:7,date:15,presult:6},
          //   {year:2000,month:7,date:30,presult:7},
          //   {year:2000,month:7,date:31,presult:1},
          //   {year:2000,month:1,date:15,presult:6},
          //   {year:2000,month:2,date:15,presult:2},
          //   {year:2000,month:11,date:15,presult:3},
          //   {year:2000,month:12,date:15,presult:5},
          //   {year:1920,month:7,date:15,presult:4},
          //   {year:1921,month:7,date:15,presult:5},
          //   {year:2048,month:7,date:15,presult:3},
          //   {year:2049,month:7,date:15,presult:4}
          // ];
          this.$axios.get('/getCalendarData1')
            .then((response) => {
              this.tableData=response.data;
              for(let i=0;i<this.tableData.length;i++){
                this.$axios.post('/calendarTest',
                  {
                    'year':this.tableData[i].year,
                    'month':this.tableData[i].month,
                    'date':this.tableData[i].date,
                    'index':i
                  })
                  .then((response) => {
                    let result=response.data;
                    this.changeData(result)
                  })
              }
            });
        },
        calendarTest2(){
          this.tableCol=[
            {name:"year", value:"year"},
            {name:"month", value:"month"},
            {name:"date", value:"date"},
            {name:"预期结果", value:"presult"},
            {name:"测试结果", value:"rresult"},
            {name:"正误", value:"tf"},
          ];
          // this.tableData=[
          //   {year:2007,month:2,date:25,presult:7},
          //   {year:2008,month:2,date:28,presult:4},
          //   {year:2005,month:5,date:30,presult:1},
          //   {year:1990,month:4,date:18,presult:3},
          //   {year:"year",month:96,date:31,presult:"error"},
          //   {year:1935,month:3,date:201,presult:"error"},
          //   {year:1895,month:10,date:31,presult:"error"},
          //   {year:2051,month:2,date:1,presult:"error"},
          //   {year:2005,month:0,date:1,presult:"error"},
          //   {year:2008,month:0,date:1,presult:"error"},
          //   {year:2005,month:13,date:1,presult:"error"},
          //   {year:1999,month:1,date:0,presult:"error"},
          //   {year:2007,month:2,date:30,presult:"error"},
          //   {year:2008,month:2,date:31,presult:"error"},
          //   {year:1998,month:1,date:32,presult:"error"},
          //   {year:1990,month:4,date:33,presult:"error"}
          // ];
          // for(let i=0;i<this.tableData.length;i++){
          //   this.$axios.post('/calendarTest',
          //     {
          //       'year':this.tableData[i].year,
          //       'month':this.tableData[i].month,
          //       'date':this.tableData[i].date,
          //       'index':i
          //     })
          //     .then((response) => {
          //       let result=response.data;
          //       this.changeData(result)
          //     })
          // }
          this.$axios.get('/getCalendarData2')
            .then((response) => {
              this.tableData=response.data;
              for(let i=0;i<this.tableData.length;i++){
                this.$axios.post('/calendarTest',
                  {
                    'year':this.tableData[i].year,
                    'month':this.tableData[i].month,
                    'date':this.tableData[i].date,
                    'index':i
                  })
                  .then((response) => {
                    let result=response.data;
                    this.changeData(result)
                  })
              }
            });
        },
      phoneTest1(){
        this.tableCol=[
          {name:"本月通话分钟数", value:"n"},
          {name:"本年度未按时缴费次数", value:"m"},
          {name:"预期结果", value:"presult"},
          {name:"测试结果", value:"rresult"},
          {name:"正误", value:"tf"},
        ];
        // this.tableData=[
        //   {n:150,m:-1,presult:"error"},
        //   {n:150,m:0,presult:47.05},
        //   {n:150,m:1,presult:47.05},
        //   {n:150,m:6,presult:47.50},
        //   {n:150,m:10,presult:47.50},
        //   {n:150,m:11,presult:47.50},
        //   {n:150,m:12,presult:"error"},
        //   {n:-1,m:6,presult:"error"},
        //   {n:0,m:6,presult:25.00},
        //   {n:60,m:6,presult:34.00},
        //   {n:40000,m:6,presult:5845.00},
        //   {n:44640,m:6,presult:6520.12},
        //   {n:45000,m:6,presult:"error"},
        // ];
        this.$axios.get('/phoneBillTest1')
          .then((response) => {
            this.tableData=response.data;
            for(let i=0;i<this.tableData.length;i++){
              this.$axios.post('/phoneBillTest',
                {
                  'n':this.tableData[i].n,
                  'm':this.tableData[i].m,
                  'index':i
                })
                .then((response) => {
                  let result=response.data;
                  this.changeData(result)
                })
            }
          });

      },
      phoneTest2(){
        this.tableCol=[
          {name:"本月通话分钟数", value:"n"},
          {name:"本年度未按时缴费次数", value:"m"},
          {name:"预期结果", value:"presult"},
          {name:"测试结果", value:"rresult"},
          {name:"正误", value:"tf"},
        ];
        // this.tableData=[
        //   {n:30,m:1,presult:29.455},
        //   {n:90,m:2,presult:38.2975},
        //   {n:150,m:3,presult:47.05},
        //   {n:240,m:5,presult:61.00},
        //   {n:360,m:9,presult:79.00},
        // ];
        this.$axios.get('/phoneBillTest2')
          .then((response) => {
            this.tableData=response.data;
            for(let i=0;i<this.tableData.length;i++){
              this.$axios.post('/phoneBillTest',
                {
                  'n':this.tableData[i].n,
                  'm':this.tableData[i].m,
                  'index':i
                })
                .then((response) => {
                  let result=response.data;
                  this.changeData(result)
                })
            }
          });
      },
      phoneTest3(){
        this.tableCol=[
          {name:"本月通话分钟数", value:"n"},
          {name:"本年度未按时缴费次数", value:"m"},
          {name:"预期结果", value:"presult"},
          {name:"测试结果", value:"rresult"},
          {name:"正误", value:"tf"},
        ];
        // this.tableData=[
        //   {n:30,m:0,presult:29.455},
        //   {n:30,m:6,presult:29.50},
        //   {n:90,m:0,presult:38.2975},
        //   {n:90,m:6,presult:38.50},
        //   {n:150,m:0,presult:47.05},
        //   {n:150,m:6,presult:47.50},
        //   {n:240,m:0,presult:60.10},
        //   {n:240,m:6,presult:61.00},
        //   {n:360,m:0,presult:77.38},
        //   {n:360,m:9,presult:79.00},
        // ];
        this.$axios.get('/phoneBillTest3')
          .then((response) => {
            this.tableData=response.data;
            for(let i=0;i<this.tableData.length;i++){
              this.$axios.post('/phoneBillTest',
                {
                  'n':this.tableData[i].n,
                  'm':this.tableData[i].m,
                  'index':i
                })
                .then((response) => {
                  let result=response.data;
                  this.changeData(result)
                })
            }
          });
      },
      phoneTest4(){
        this.tableCol=[
          {name:"本月通话分钟数", value:"n"},
          {name:"本年度未按时缴费次数", value:"m"},
          {name:"预期结果", value:"presult"},
          {name:"测试结果", value:"rresult"},
          {name:"正误", value:"tf"},
        ];
        // this.tableData=[
        //   {n:150,m:-1,presult:"error"},
        //   {n:-1,m:6,presult:"error"},
        //   {n:30,m:0,presult:29.455},
        //   {n:30,m:6,presult:29.50},
        //   {n:90,m:0,presult:38.2975},
        //   {n:90,m:6,presult:38.50},
        //   {n:150,m:0,presult:47.05},
        //   {n:150,m:6,presult:47.50},
        //   {n:240,m:0,presult:60.10},
        //   {n:240,m:6,presult:61.00},
        //   {n:360,m:0,presult:77.38},
        //   {n:360,m:9,presult:79.00},
        //   {n:45000,m:6,presult:"error"},
        //   {n:150,m:12,presult:"error"},
        // ];
        this.$axios.get('/phoneBillTest4')
          .then((response) => {
            this.tableData=response.data;
            for(let i=0;i<this.tableData.length;i++){
              this.$axios.post('/phoneBillTest',
                {
                  'n':this.tableData[i].n,
                  'm':this.tableData[i].m,
                  'index':i
                })
                .then((response) => {
                  let result=response.data;
                  this.changeData(result)
                })
            }
          });
      },
        changeData(result){
            this.$set(this.tableData[result['index']],'rresult',result['result']);
            if(result['result'] == this.tableData[result['index']]['presult']){
                this.tableData[result['index']]['tf']="正确"
            }
            else{
                this.tableData[result['index']]['tf']="错误"
            }
        }
    }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
