export const actionTypes = {
  FETCH_ALL_JOBS: 'fetch_all_jobs',
  TRACK_ITEM: 'track_item',
  UPDATE_ITEM: 'update_item'
}
export const mutationTypes = {
  UPDATE_JOB_LIST: 'update_job_list',
  UPDATE_JOB_ITEM: 'update_job_item'
}
export const getterTypes = {
  JOB_PER_ID: 'job_per_id'
}

export const state = () => ({
  jobs: []
})

export const actions = {
  async [actionTypes.FETCH_ALL_JOBS]({ commit }) {
    const jobs = await this.$axios.$get('/job')
    commit(mutationTypes.UPDATE_JOB_LIST, jobs)
  },
  async [actionTypes.TRACK_ITEM]({ commit }, { job, id: idToTrack }) {
    const item = await this.$axios.$get(`/item/${idToTrack}`)
    item.job = job.id
    const url = `/item/${item.item_id}/`
    await this.$axios.$put(url, item)
  },
  async [actionTypes.UPDATE_ITEM]({ commit }, updatedItem) {
    const url = `/item/${updatedItem.item_id}/`
    let res = null
    try {
      res = await this.$axios.$put(url, updatedItem)
      commit(mutationTypes.UPDATE_JOB_ITEM, updatedItem)
    } catch (e) {
      res = e.message
    }
    return res
  }
}
export const mutations = {
  [mutationTypes.UPDATE_JOB_LIST](state, jobs) {
    state.jobs = [...jobs]
  },
  [mutationTypes.UPDATE_JOB_ITEM](state, updatedItem) {
    const job = state.jobs.find((el) => el.id === updatedItem.job)
    job.current_items = [
      ...job.current_items.filter((el) => el.item_id !== updatedItem.item_id),
      updatedItem
    ]
  }
}
export const getters = {
  [getterTypes.JOB_PER_ID]: (state) => (id) =>
    state.jobs.find((job) => job.id === id)
}
